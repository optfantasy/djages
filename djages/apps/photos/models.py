""" Photo models """

import datetime
import logging
import urllib
import uuid, os, re
import hashlib

from django.core.files import File
from django.core.files.storage import DefaultStorage
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField, SetField, EmbeddedModelField
from django.db.models.signals import post_save, post_delete, pre_delete
from django.db.models import F
from django.utils.encoding import smart_str

from globals.utils import get_django_ct, get_upload_path_fun
from globals.contrib import MongoDBManager
from imagekit.lib import Image
from photos.imagespecs import *


class ImageInfo(models.Model):
    ensure_cache    = models.BooleanField(default=False)
    width           = models.FloatField(default=0)
    height          = models.FloatField(default=0)
    filesize        = models.IntegerField(default=0)

    def set_field(self, target_id, target_class, field, field_value):
        if field not in ('ensure_cache', 'width', 'height', 'filesize'):
            raise LookupError

        target_class.objects.set('_img_info.'+field, target_id, field_value)
        setattr(self, field, field_value)

    def to_json(self):
        rtn = {
            'notify_sound': self.notify_sound,
            'notify_vibration': self.notify_vibration,
            'message_prview': self.message_prview
        }
        return rtn

    def __unicode__(self):
        display_list = []
        for field in self._meta.fields:
            if field.name is 'id':
                continue
            display_list.append(field.name+': %s' % self.__dict__[field.name])
        return ', '.join(display_list)


def imagespecfilter(x, baseclass):
    return issubclass(x.__class__, baseclass)


class BaseImageModel(models.Model):
    """ Abstract image base class """
    _img_info      = EmbeddedModelField('ImageInfo', null=True)
    
    # original        = ImageJpeg()
    # use_default    = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

    @property
    def image_info(self):
        if not self._img_info:
            self._img_info = ImageInfo()
            self.__class__.objects.filter(id=self.id).update(_img_info=self._img_info)

        return self._img_info

    def get_filesize(self):
        # Lazy build filesize
        if self.image_info.filesize == 0:
            self.image_info.set_field(self.id, self.__class__, 'filesize', self.image.size)

        return self.image_info.filesize

    def save(self, *args, **kwargs):
        if self.image:
            self.image_info.set_field(self.id, self.__class__, 'width', self.image.width)
            self.image_info.set_field(self.id, self.__class__, 'height', self.image.height)
            self.get_filesize()
            self._ensure_cache()

        super(BaseImageModel, self).save(*args, **kwargs)

    def has_ensured_cache(self):
        return self.image_info.ensure_cache

    def use_default_img(self):
        raise NotImplementedError

    def _ensure_cache(self, force=False):
        if self.has_ensured_cache() and not force:
            return

        for key in self.img_list:
            obj = getattr(self, key)
            if not os.path.exists(obj.path):
                obj.generate()
                
        self.image_info.set_field(self.id, self.__class__, 'ensure_cache', True)

    def delete(self, *args, **kwargs):
        if not self.use_default_img():
            for spec_file in self._ik.spec_files:
                spec_file.clear()
            
            # remove image file
            try:
                os.remove(self.image.path)
            except OSError as err:
                print err

        super(BaseImageModel, self).delete(*args, **kwargs)


class InvalidImageException(Exception):
    pass

