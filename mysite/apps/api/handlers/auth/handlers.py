from django.contrib.auth import authenticate, login, logout
from django.core.validators import email_re
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth import login as auth_login
import api.errors as api_errors
from api.handlers.global_handler import GlobalBaseHandler

class LogoutHandler(GlobalBaseHandler):
    
    def create(self, request):
        logout(request)
        return

class SigninHandler(GlobalBaseHandler):
    required_fields = ('username', 'password', 'remember_me')
    create_auth_exempt = True
    
    def create(self, request):
        # Enables user to log in by either username or email
        name_email = request.CLEANED['username']
        query = {'email__iexact': name_email} if email_re.match(name_email) else {'username__iexact': name_email}
        
        errors = {}
        username = ''
        try:
            user = User.objects.get(**query)
            username = user.username
        except User.DoesNotExist:
            raise api_errors.GlobalAPIException(api_errors.ERROR_AUTH_USERNAME_NOT_EXIST)

        """ Logs a user in and returns a session key. """
        password = request.CLEANED['password']
        remember_me = request.CLEANED['remember_me']

        user = authenticate(username=username, password=password)
        if not user:
            raise api_errors.GlobalAPIException(api_errors.ERROR_USER_PASSWORD_NOT_MATCH)
            errors['password'] = "The password you entered is incorrect."

            rtn = {
                "errors": errors
            }

            return rtn
        
        if remember_me=='true':
            request.session.set_expiry(1209600)

        if user.is_active:
            auth_login(request, user)
            rtn = {
                    "user_id": user.id,
                    }
            return rtn
            
        else:
            return False
    