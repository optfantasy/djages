import uuid
import hashlib
import smtplib
import datetime
from random import shuffle

from django.db import models
from django.core.files import File
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

from globals.contrib import MongoDBManager

from djangotoolbox.fields import ListField, DictField, SetField, EmbeddedModelField
from imagekit.lib import Image

from django.core.urlresolvers import reverse

from globals.timezones import TIMEZONE_CHOICES
from photos.models import Photo


class UserProfileManager(MongoDBManager):

    def get_anonymous(self):
        anonymous = User.objects.get(username='AnonymousUser')
        return anonymous   
    

class UserProfile(models.Model):

    user = models.ForeignKey(User, related_name="userprofile")
    image = models.ImageField(upload_to=get_upload_path_fun('userprofile'))
    full_name = models.CharField(max_length=60, null=True, blank=True)
    timezone = models.CharField(max_length=100, choices=TIMEZONE_CHOICES, default="Asia/Taipei")

    # Collection: Basics
    user_agent = models.TextField(null=True, blank=True) # from HTTP header

    objects = UserProfileManager()
    
    def __unicode__(self):
        return self.user.username
    
    def get_accept_language(self):
        if self.accept_language:
            return self.accept_language.split(',')[0]
        else:
            return 'en'

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        elif not (self.user.first_name and self.user.last_name):
            return ''
        else:
            return "%s %s" % (self.user.first_name, self.user.last_name)
    
    def get_display_name(self, **kwargs):
        fullname = self.get_full_name()
        if fullname:
            return fullname
        else:
            return self.user.username
            
    def get_display_photo(self):
        return self.i125
    
    def get_display_photo_url(self, size='i125'):
        return getattr(self, size).url
    
    def username(self):
        return self.user.username

    def email(self):
        return self.user.email
    
    
    def to_json(self, request=None, detail=False, simple=False, **kwargs):
        rtn = {
            'id': self.user.pk,
            'full_name': self.get_display_name(),
            'username': self.user.username,
            'email': self.user.email,
            'photo': self.get_display_photo_url(),
        }

        return rtn
    

def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created'] == True:
        up = UserProfile.objects.create(user=user)
        user_fallback = '%s/images/%s' % (settings.GLOBALS_STATIC_ROOT, 'img_user_fallback.png')
        image.verify()
        fp = open(user_fallback,'r')
        target_file = File(fp)
        name = 'img_user_fallback.png'
        up.image.save(name, target_file, save=True)
        fp.close()

post_save.connect(create_profile, sender=User)

def on_delete_user(sender, **kwargs):
    user = kwargs['instance']
    UserProfile.objects.filter(user=user).delete()
    
pre_delete.connect(on_delete_user, sender=User)

