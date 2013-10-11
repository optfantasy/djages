from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

import api.errors as api_errors

def validate_target(target_type, target_id, type_mappings):
    """ Ensures content type and object for target type and id exist.
    
    For example:
    
    >>> type_mappings = {'post': Post, 'review': Review}
    >>> pk = "4e9d51f10218231314000494"
    >>> target = validate_target('post', pk, type_mappings)
    
    :param target_type: Target object type, should be a key in type_mappings
    :type target_type: string
    :param target_id: PK of target object
    :type target_id: string
    :param type_mappings: Dictionary of type -> model mappings for content type lookups
    :type type_mappings: dict
    :return: Target object, if found
    :rtype: object
    :raises GlobalAPIException(ERROR_GENERAL_BAD_TYPE): If target type can not be found
    :raises GlobalAPIException(ERROR_GENERAL_TARGET_NOT_FOUND): If target object could not
        be found
    """
    try:
        klass = type_mappings[target_type]
        target_type = ContentType.objects.get_for_model(klass)
    except KeyError:
        raise api_errors.GlobalAPIException(api_errors.ERROR_GENERAL_BAD_TYPE)

    try:
        target = klass.objects.get(pk=target_id)
    except klass.DoesNotExist:
        raise api_errors.GlobalAPIException(api_errors.ERROR_GENERAL_TARGET_NOT_FOUND)

    return target

def validate_user(user_id):
    """ Ensures the user with user_id exists.
    
    :param user_id: Id of user to query
    :type user_id: string
    :return: User object, if found
    :rtype: object
    :raises GlobalAPIException(ERROR_USER_NOT_FOUND): If user could not be found
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise api_errors.GlobalAPIException(api_errors.ERROR_GENERAL_USER_NOT_FOUND)
    
    return user
