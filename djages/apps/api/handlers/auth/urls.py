from django.conf.urls.defaults import *

from api.resources import GlobalResource

from handlers import SigninHandler, LogoutHandler

urlpatterns = patterns('',
    url(r'^logout/?$', GlobalResource(handler=LogoutHandler)),
    url(r'^signin/?$', GlobalResource(handler=SigninHandler)),
)
