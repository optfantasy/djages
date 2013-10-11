""" Gulu auth backends """

from django.conf import settings
from django.contrib.auth import models, backends
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

class SessionBackend(backends.ModelBackend):
    def authenticate(self, session_id=None):
        try:
            user_session = Session.objects.get(pk=session_id)
            uid = user_session.get_decoded().get('_auth_user_id')
            user = User.objects.get(id=uid)
            return user
        except Session.DoesNotExist:
            return None


class CaseInsensitiveModelBackend(backends.ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username__iexact=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
