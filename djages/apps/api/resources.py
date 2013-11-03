import sys, traceback
import httplib

from django.core.signals import got_request_exception
from django.http import Http404, HttpResponse, HttpResponseServerError, HttpResponseNotAllowed
from django.utils import simplejson
from django.views.debug import ExceptionReporter
from django.views.decorators.vary import vary_on_headers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings

from bson.objectid import InvalidId
from piston.doc import HandlerMethod
from piston.emitters import Emitter
from piston.handler import typemapper
from piston.resource import Resource
from piston.utils import rc, translate_mime, MimerDataException, HttpStatusCode,\
    format_error

from api import errors as api_errors
from api.utils import process_request

def make_error_response(code, debug=None):
    """ Creates an error response for error code `code`.  If code is invalid, returns
    the default 'unknown error' response. """
    try:
        error_code, error_message = code, api_errors.API_ERRORS[code]
    except KeyError:
        error_code, error_message = api_errors.ERROR_GENERAL_UNKNOWN_ERROR,\
            api_errors.API_ERRORS[api_errors.ERROR_GENERAL_UNKNOWN_ERROR]
    
    content = {
        'success': False,
        'error': {
            'code': error_code,
            'message': error_message,
        }
    }
    if debug:
        content['error']['debug'] = debug
    
    result = rc.ALL_OK
    result.content = content

    return result

CHALLENGE = object()

class GlobalResource(Resource):
    
    @vary_on_headers('Authorization')
    def __call__(self, request, *args, **kwargs):
        rm = request.method.upper()
        handler, anonymous = self.handler, self.handler.is_anonymous
        
        if rm == 'PUT' and request.META['CONTENT_TYPE']=="application/json":
            rm = request.method = 'POST'
        
        # Translate nested datastructs into `request.data` here.
        if rm == 'POST':
            try:
                translate_mime(request)
            except MimerDataException:
                return rc.BAD_REQUEST
            if not hasattr(request, 'data'):
                request.data = request.POST
        if not rm in handler.allowed_methods:
            return HttpResponseNotAllowed(handler.allowed_methods)

        meth = getattr(handler, self.callmap.get(rm, ''), None)
        if not meth:
            raise Http404

        # Clean up the request object a bit, since we might
        # very well have `oauth_`-headers in there, and we
        # don't want to pass these along to the handler.

        request = self.cleanup_request(request)

        try:
            # The verified process of new api is all in process_request
            request = process_request(handler, request, *args, **kwargs)
            raw_response = meth(request, *args, **kwargs)
            # An implicit protocal for deliver info from handler
            if type(raw_response)==dict and raw_response.has_key('_info') and raw_response.has_key('_response'):
                result = {
                    'success': True,
                    'response': raw_response['_response'],
                    'info': raw_response['_info'],
                }
            else:
                result = {
                    'success': True,
                    'response': raw_response,
                    'info': {}
                }
        except Exception, e:
            result = self.error_handler(e, request, meth)

        emitter, ct = Emitter.get('json')
        fields = handler.fields

        if hasattr(handler, 'list_fields') and isinstance(result, (list, tuple, QuerySet)):
            fields = handler.list_fields

        status_code = 200
        
        # If we're looking at a response object which contains non-string
        # content, then assume we should use the emitter to format that 
        # content
        if isinstance(result, HttpResponse) and not result._is_string:
            status_code = result.status_code
            # Note: We can't use result.content here because that method attempts
            # to convert the content into a string which we don't want. 
            # when _is_string is False _container is the raw data
            result = result._container
     
        srl = emitter(result, typemapper, handler, fields, anonymous)

        try:
            """
            Decide whether or not we want a generator here,
            or we just want to buffer up the entire result
            before sending it to the client. Won't matter for
            smaller datasets, but larger will have an impact.
            """
            if self.stream: stream = srl.stream_render(request)
            else: stream = srl.render(request)

            if not isinstance(stream, HttpResponse):
                resp = HttpResponse(stream, mimetype=ct, status=status_code)
            else:
                resp = stream

            resp.streaming = self.stream

            return resp
        except HttpStatusCode, e:
            return e.response
    
    def error_handler(self, e, request, meth):
        """
        Override this method to add handling of errors customized for your 
        needs
        """
        debug_msg = None

        if request.REQUEST.get('debug') or settings.DEBUG:
            debug_msg = e.debug if isinstance(e, api_errors.GlobalAPIException) and e.debug else unicode(e)
            exc_type, exc_value, tb = sys.exc_info()
            print '%s\n' % ''.join(traceback.format_exception(exc_type, exc_value, tb, 20))
        
        if isinstance(e, TypeError):
            result = rc.ALL_OK
            hm = HandlerMethod(meth)
            sig = hm.signature

            msg = 'Method signature does not match.\n\n'

            if sig:
                msg += 'Signature should be: %s' % sig
            else:
                msg += 'Resource does not expect any parameters.'

            if self.display_errors:
                msg += '\n\nException was: %s' % str(e)

            result.content = simplejson.dumps({
                'success': False,
                'error': {
                    'code': api_errors.ERROR_GENERAL_BAD_SIGNATURE,
                    'message': msg,
                }
            }, ensure_ascii=False, indent=3)
            return result
        
        elif isinstance(e, Http404):
            return make_error_response(api_errors.ERROR_GENERAL_NOT_FOUND)
 
        elif isinstance(e, api_errors.GlobalAPIException):
            return make_error_response(e.code, debug_msg)
            
        elif isinstance(e, User.DoesNotExist):
            return make_error_response(api_errors.ERROR_GENERAL_USER_NOT_FOUND, debug_msg)

        elif isinstance(e, InvalidId):
            return make_error_response(api_errors.ERROR_GENERAL_BAD_ID_FORMAT, debug_msg)
        
        elif isinstance(e, ObjectDoesNotExist):
            return make_error_response(api_errors.ERROR_GENERAL_TARGET_NOT_FOUND, debug_msg)
        
        else: 
            """
            On errors (like code errors), we'd like to be able to
            give crash reports to both admins and also the calling
            user. There's two setting parameters for this:

            Parameters::
             - `PISTON_EMAIL_ERRORS`: Will send a Django formatted
               error email to people in `settings.ADMINS`.
             - `PISTON_DISPLAY_ERRORS`: Will return a simple traceback
               to the caller, so he can tell you what error they got.

            If `PISTON_DISPLAY_ERRORS` is not enabled, the caller will
            receive a basic "500 Internal Server Error" message.
            """
            # report the error to django
            got_request_exception.send(sender=self, request=request)
            
            exc_type, exc_value, tb = sys.exc_info()
            rep = ExceptionReporter(request, exc_type, exc_value, tb.tb_next)
            if self.email_errors:
                self.email_exception(rep)
            if self.display_errors:
                return make_error_response(api_errors.ERROR_GENERAL_UNKNOWN_ERROR, debug_msg)
                # return HttpResponseServerError(
                #     format_error('\n'.join(rep.format_exception())))
            else:
                return make_error_response(api_errors.ERROR_GENERAL_UNKNOWN_ERROR)
