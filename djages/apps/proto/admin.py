from django.contrib import admin
from models import Proto

class ProtoAdmin(admin.ModelAdmin):
    list_display = ('title', )
    raw_id_fields = ()

admin.site.register(Proto, ProtoAdmin)
