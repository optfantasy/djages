from api.errors import GlobalAPIException
from api.handlers.global_handler import GlobalBaseHandler, GlobalIndexHandler, GlobalObjectHandler
from api.utils import process_latlon, process_boolean, process_float, create_sys_request
from proto.models import Proto


class ProtoBaseHandler(GlobalBaseHandler):
    allowed_methods = ('GET',)
    read_kwargs = ()
    read_auth_exempt = True

    def read_validate(self, query_dict, **kwargs):
        pass

    def read(self, request):
        return {'testing': True}


class ProtoIndexHandler(GlobalIndexHandler):
    query_model = Proto
    allowed_methods = ('GET',)
    read_auth_exempt = True


class ProtoObjectHandler(GlobalObjectHandler):
    query_model = Proto
    allowed_methods = ('GET',)
    read_auth_exempt = True

