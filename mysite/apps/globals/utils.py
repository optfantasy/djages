import os
import hashlib
from django.core.urlresolvers import reverse

def get_django_ct(content_type):
    if not content_type:
        return None
    django_ct = '%s.%s' % (content_type.app_label, content_type.model)
    return django_ct


def slugreverse(user, viewname, urlconf=None, args=None, kwargs=None, current_app=None):
    """ Reverses a view to a slug-based URL for user pages.

    Args:
        user: django User obj

        For other arguments see the django.core.urlresolvers.reverse

    Returns:
        A slug-based URL.
    """
    url = reverse(viewname, urlconf, args, kwargs, current_app)

    return "/%s/%s" % (user.get_profile().slug.slug, "/".join(url.split("/")[3:]))

def get_upload_path_fun(root):

    def fun(instance, filename):
        filename = filename.replace('%','_')
        name_hash = hashlib.md5(filename).hexdigest()
        return os.path.join(root, name_hash[0:2], name_hash[2:4], name_hash[4:6], name_hash[6:8], filename)

    return fun