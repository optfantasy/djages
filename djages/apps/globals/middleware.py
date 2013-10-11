import re
from django.shortcuts import render_to_response
from django.template import RequestContext

URL_IGNORE = ['media', 'static',]

class MobileDetectMiddleware(object):
    """
    Attempt to detect mobile browsers.

    A better implementation would probably be based on
    http://wurfl.sourceforge.net/
    or
    http://www.zytrax.com/tech/web/mobile_ids.html
    """

    ipadRE = re.compile(r'ipad', re.IGNORECASE)
    mobileRE = re.compile(r'android|fennec|iemobile|iphone|ipad|ipod|opera (?:mini|mobi)', re.IGNORECASE)
    androidRE = re.compile(r'android|fennec|iemobile|opera (?:mini|mobi)', re.IGNORECASE)
    NOT_SUPPORTED_LIST = ('MSIE 6', 'MSIE 7', 'MSIE 8')

    def process_request(self, request):
        path = request.path.split('/')
        if path[1] in URL_IGNORE:
            return
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if filter(lambda x: x in user_agent, self.NOT_SUPPORTED_LIST):
            return render_to_response('ienotsupport.html', context_instance = RequestContext(request))

        request.mobile_browser = bool(self.mobileRE.search(request.META.get('HTTP_USER_AGENT', '')))
        request.is_android = bool(self.androidRE.search(request.META.get('HTTP_USER_AGENT', '')))
        request.is_ipad = bool(self.ipadRE.search(request.META.get('HTTP_USER_AGENT', '')))



class TranslateMiddleware(object):
    def process_response(self, request, response):
        path = request.path.split('/')
        if path[1] in URL_IGNORE:
            return response
        try:
            user_profile = request.user.get_profile()
        except:
            user_profile = None

        if user_profile:
            if user_profile.accept_language:
                request.session['django_language'] = user_profile.accept_language.split(",")[0].lower()
        else:
            pass

        return response



