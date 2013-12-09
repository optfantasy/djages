from django.contrib.auth.models import User
from django.conf import settings
from hashlib import sha256
from django.db.models.signals import post_save
from django.db import models as django_models
from django.core.exceptions import ObjectDoesNotExist
from globals.contrib import MongoDBManager


def get_profile(self):
    try:
        pf = User._get_profile(self)
        return pf
    except ObjectDoesNotExist:
        from models import UserProfile
        pf, created = UserProfile.objects.create_user_profile(user=self)
        print 'create it'
        return pf

def get_display_name(self):
    return self.get_profile().get_display_name()

def to_json(self, simple=None, **kwargs):
    extra_query_fields= kwargs.get('extra_query_fields')
    image_spec = kwargs.get('image_spec')
    
    if simple:
        # TODO: optimize this
        rtn = {
            'id': self.id,
            'username': self.username,
            'nickname': self.get_profile().get_display_name(),
        }
        
        return rtn
    else:
        return self.get_profile().to_json(**kwargs)

def is_user(self):
    return True

def is_first_login(self):
    return self.get_profile().is_first_login


User.add_to_class("_get_profile", User.get_profile)
User.add_to_class("get_profile", get_profile)
User.add_to_class("full_name", django_models.CharField(max_length=50))
User.add_to_class("get_display_name", get_display_name)
User.add_to_class('is_user', is_user)
User.add_to_class('to_json', to_json)
User.add_to_class('is_first_login', is_first_login)
User.add_to_class('mongo_objects', MongoDBManager())
