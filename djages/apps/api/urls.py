from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^auth/', include('api.handlers.auth.urls')),
    (r'^proto/', include('api.handlers.proto.urls')),
)
