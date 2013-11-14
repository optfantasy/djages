from djangotoolbox.fields import AbstractIterableField
from django.contrib.auth.models import User

def dummy(self, **kwargs):
	pass

AbstractIterableField.formfield = dummy

def create_anonymous_user(**kwargs):
    """ Creates anonymous User instance. """
    try:
        User.objects.get(username="AnonymousUser")
    except User.DoesNotExist:
        User.objects.create(username='AnonymousUser')
    except User.MultipleObjectsReturned:
        for u in User.objects.filter(username="AnonymousUser")[1:]:
            u.delete()

create_anonymous_user()