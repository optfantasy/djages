import json

from piston.handler import BaseHandler

from api.utils import process_latlon, process_integer

# ============== Operation Handler =============
class GlobalBaseHandler(BaseHandler):
    """This handler is s a base handler for global.
    """
    # Allowed request methods: might be 'POST', 'GET', 'DELETE'
    allowed_methods = ('POST', )

    # For POST:
    # required_fields - lists the parameters that must be specified
    # create_kwargs - only the parameters in create_kwargs will be kept. (it is a superset of required_fields)
    # files_kwargs - corresponding to request.FILES
    # form_fields - only the parameters in form_fields will be updated. (for update object)
    # perform_save - perform save operation for object update. it might cause risk condition if it is set as "True".
    #                True -> update, False -> save
    required_fields = ()
    create_kwargs = ()
    files_kwargs = ()
    form_fields = ()
    update_instead_save = False

    # For GET:
    # required_fields_for_read - lists the parameters that must be specified for read 
    # read_kwargs - only the parameters in read_kwargs will be kept.
    # allowed_filter - only the parameters in allowed_filter will be used as query params.
    # filter_opt - define several type of special query (see: notify/handlers.py).
    # para_mapping - used for mapping the read_kwargs to allowed_filter
    required_fields_for_read=()
    read_kwargs = ()
    allowed_filter = ()
    filter_opt = ()
    para_mapping = {}

    # For DELETE:
    # delete_kwargs - lists the parameters that must be specified
    delete_kwargs = ()


    # Settings:
    # query_model - model to query
    # about_privacy - if about_privacy is True, then use "viewables" to query object
    # default_order - the default sorting order, which might be "-timestamp", "updated" and so on.
    # read_auth_exempt - if this parameter is True, then the GET request of this resource is authenticatation exempt
    # create_auth_exempt - if this parameter is True, then the POST request of this resource is authenticatation exempt
    query_model = None
    about_privacy = False
    default_order = None
    read_auth_exempt = False
    create_auth_exempt = False
    superuser_only = False

    def __init__(self):
        if not self.create_kwargs:
            self.create_kwargs = self.required_fields

    def auth_resource(self, request, json_dict, **kwargs):
        # We should implement GET, POST, DELETE authentication here.
        return

    def map_para(self, query_dict):
        # Automatically strip Id from the end of input key
        for key in query_dict.keys():
            if key in self.para_mapping.keys():
                mapped_key = self.para_mapping[key]
                query_dict[mapped_key] = query_dict[key]
            elif key.endswith('_id'):
                mapped_key = key[:-3]
                query_dict[mapped_key] = query_dict[key]
        return query_dict

    def create_validate(self, query_dict, **kwargs):
        pass

    def read_validate(self, query_dict, **kwargs):
        pass

    def delete_validate(self, query_dict, **kwargs):
        pass

# ============== Index Handler =============
class GlobalIndexHandler(GlobalBaseHandler):
    """
    This handler is used to manager the url like :collection/
    It allows POST and GET method.
    We can use GET method to query objects in :collection
    and use POST to create an object belongs to this :collection
    """
    allowed_methods = ('POST', 'GET')

    def read(self, request, **kwargs):
        """ Query """
        offset = request.CLEANED['offset']
        endpoint = request.CLEANED['endpoint']

        if 'custom_query' in request.CLEANED:
            query_set = request.CLEANED['custom_query']
            del request.CLEANED['custom_query']
        elif self.about_privacy:
            query_set = self.query_model.viewables(user=request.user)
        else:
            query_set = self.query_model.objects.all()

        # query_list = []
        query_args = {}

        if not 'use_custom_only' in request.CLEANED:
            for key, value in request.CLEANED.iteritems():
                if key in self.allowed_filter:
                    if isinstance(value, basestring) and ',' in value:
                        query_args[key + '__in'] = value.split(',')
                    else:
                        query_args[key] = value

        results = query_set.filter(**query_args)
        if request.CLEANED['order_by']:
            results = results.order_by(request.CLEANED['order_by'])
        elif self.default_order:
            results = results.order_by(self.default_order)
        if kwargs.get('all'):
            return [r.to_json(request=request, detail=request.CLEANED['detail']) for r in results]
        if kwargs.get('raw'):
            return [r for r in results[offset:endpoint]]
        return [r.to_json(request=request, detail=request.CLEANED['detail']) for r in results[offset:endpoint]]


# ============== Object Handler =============
class GlobalObjectHandler(GlobalBaseHandler):
    """
    This handler is used to manage the url like :collection/:object_id
    It allows POST, GET and DELETE method.
    We can use GET method to get object of :collection/:object_id
    and use POST to update the object -- or doing some specific operation.
    Use DELETE to delete the object.
    """
    allowed_methods = ('POST', 'GET', 'DELETE')
    form_fields = ()
    update_instead_save = False

    def read(self, request, object_id, **kwargs):
        if request.CLEANED.get('_obj'):
            result = request.CLEANED.get('_obj')
        else:
            result = self.query_model.objects.get(id=object_id)
        return result.to_json(request=request, detail=request.CLEANED['detail'])

    def delete(self, request, object_id, **kwargs):
        if request.CLEANED.get('_obj'):
            result = request.CLEANED.get('_obj')
        else:
            result = self.query_model.objects.get(id=object_id)
        result.delete()
        return

    def create(self, request, object_id, **kwargs):
        changed_fields = {}
        if request.CLEANED.get('_obj'):
            result = request.CLEANED.get('_obj')
        else:
            result = self.query_model.objects.get(id=object_id)
        for key, value in request.CLEANED.iteritems():
            if value != None and key in self.form_fields:
                setattr(result, key, value)
                changed_fields[key] = value
        if changed_fields:
            if self.update_instead_save:
                self.query_model.objects.filter(id=object_id).update(**changed_fields)
            else:
                result.save()
        # return ','.join(changed_fields)
        return result.to_json(request=request, detail=True)



# ============== Attribute Handler =============
class GlobalAttributeHandler(GlobalBaseHandler):
    """
    This handler is used to manager the url like :collection/:object_id/:attribute
    It allows POST, GET and DELETE method.

    The attribute should be a ListField or SetField with IDs.

    We can use GET method to get objects for :collection/:object_id/:attribute
    and use POST to add an item from the attibute.
    Use DELETE to remove an item from the attibute.
    """
    allowed_methods = ('POST', 'GET', 'DELETE')
    required_fields = ('attr_value', )
    delete_kwargs = required_fields
    field_model = None

    def validate(self, query_dict, object_id, **kwargs):
        query_dict['target'] = self.query_model.objects.get(id=object_id)

    read_validate = validate
    create_validate = validate
    delete_validate = validate

    def read(self, request, object_id, attr):
        values = getattr(request.CLEANED['target'], attr)
        if not self.field_model:
            return list(values)
        offset = request.CLEANED['offset']
        endpoint = request.CLEANED['endpoint']
        results = self.field_model.objects.filter(id__in=values)
        return [r.to_json(request=request, detail=request.CLEANED['detail']) for r in results[offset:endpoint]]

    def delete(self, request, object_id, attr):
        raise NotImplementedError("Implement delete method.")

    def create(self, request, object_id, attr):
        raise NotImplementedError("Implement create method.")



