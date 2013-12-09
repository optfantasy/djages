from hashlib import sha256
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django import forms
from django.conf import settings
from user_profiles.models import UserProfile
from imagekit.admin import AdminThumbnail


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'full_name', 'admin_thumbnail')
	raw_id_fields = ('user',)
	search_fields = ['username']
	readonly_fields = ('_img_info', )
	list_per_page = 100
	admin_thumbnail = AdminThumbnail(image_field='i50')
	# actions = [delete_regristration_and_user, ]


admin.site.register(UserProfile, UserProfileAdmin)


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'last_login', 'date_joined', )

class CustomUserAdmin(UserAdmin):
	fieldsets = None
	form = UserForm
	list_filter = ()
	ordering = ('-date_joined', )
	search_fields = ('username', 'email')
	list_display = ('username', 'is_active', 'is_staff', 'email', 'first_name', 'last_name', 'last_login', 'date_joined')

	# Override the original bulk delete to ensure the system is working correctly.
	actions=['really_delete_selected']
	
	def get_actions(self, request):
	    actions = super(CustomUserAdmin, self).get_actions(request)
	    del actions['delete_selected']
	    return actions
	    
	def really_delete_selected(self, request, queryset):
	    for obj in queryset:
	        obj.delete()

	    if queryset.count() == 1:
	        message_bit = "1 user was"
	    else:
	        message_bit = "%s user entries were" % queryset.count()
	    self.message_user(request, "%s successfully deleted." % message_bit)
	really_delete_selected.short_description = "Delete selected entries"


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

