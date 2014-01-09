from django.conf import settings
from haystack import indexes

from models import Proto
from queued_search.indexes import QueuedSearchIndex
from search.utils import word_analize, name_seperate
from search.fields import MaxWordField

if settings.REAL_TIME_SEARCH_INDEX:
    SEARCH_INDEX_TYPE = QueuedSearchIndex if settings.USE_REDIS_QUEUE else indexes.RealTimeSearchIndex
else:
    SEARCH_INDEX_TYPE = indexes.SearchIndex


class ProtoIndex(SEARCH_INDEX_TYPE, indexes.Indexable):
    text = MaxWordField(document=True)
    name = indexes.CharField(model_attr='name')
    lon = indexes.FloatField(model_attr='lon')
    lat = indexes.FloatField(model_attr='lat')
    latlon = indexes.LocationField()

    def get_model(self):
        return Proto

    def index_queryset(self):
        return Proto.objects.all()

    def prepare(self, obj):
        self.prepared_data = super(ProtoIndex, self).prepare(obj)
        self.prepared_data['latlon'] = str(obj.lat) + ',' + str(obj.lon)
        
        return self.prepared_data

    def prepare_text(self, obj):
        return ''

