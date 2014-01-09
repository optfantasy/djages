from django.conf.urls.defaults import *

from api.resources import GlobalResource
from handlers import ProtoIndexHandler, ProtoObjectHandler

urlpatterns = patterns('',
    url(r'^$', GlobalResource(handler=ProtoIndexHandler)),
    url(r'^(?P<object_id>[\w\-\_]+)/?$', GlobalResource(handler=ProtoObjectHandler)),
)
