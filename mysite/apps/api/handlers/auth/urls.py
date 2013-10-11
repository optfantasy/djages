from django.conf.urls.defaults import *

from api.resources import GuluResource

from handlers import SigninHandler, LogoutHandler

urlpatterns = patterns('',
    url(r'^logout/?$', GuluResource(handler=LogoutHandler)),
    url(r'^signin/?$', GuluResource(handler=SigninHandler)),
)
