from django.db import models
from django.db.models.signals import pre_delete
from django.utils.translation import ugettext_lazy as _

from djangotoolbox.fields import ListField, DictField
from django_mongodb_engine.contrib import MongoDBManager

# Change Proto to your model name

class ProtoManager(MongoDBManager):
	pass
            

class Proto(models.Model):
    title = models.CharField(max_length=120)
    objects = ProtoManager()

    def __unicode__(self):
    	return self.id

    def to_json(self, request=None, detail=False, **kwargs):
    	return {'title': self.title}

    class Meta:
    	pass
        # get_latest_by = 'created'


# def before_delete(sender, **kwargs):
#     obj = kwargs['instance']
#     # obj is your model

# pre_delete.connect(before_delete, sender=Proto)

