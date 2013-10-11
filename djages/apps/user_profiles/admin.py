from hashlib import sha256
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django import forms
from django.conf import settings
from user_profiles.models import UserProfile, BindingPhone
# from registration.models import Registration
from slug.models import Slug

# def delete_regristration_and_user(modeladmin, request, queryset):
# 	for up in queryset:
# 		user = up.user
# 		Registration.objects.filter(user=user).delete()
# 		Slug.objects.filter(object_id=user.id).delete()
# 		up.delete()
# 		user.delete()
# delete_regristration_and_user.short_description = "Delete user_profile, registration, and user object."

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'full_name', 'get_setting', 'other_emails', 'current_lang')
	raw_id_fields = ('user', 'main_profile_pic', 'slug')
	search_fields = ['username', 'phone_sms', 'phone_sms_e164']
	list_per_page = 100
	# actions = [delete_regristration_and_user, ]


admin.site.register(UserProfile, UserProfileAdmin)

class BindingPhoneAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone_sms_e164', 'code', '_codes', 'valid', 'created', )
	raw_id_fields = ('user', )
	search_fields = ['phone_sms_e164']
	list_per_page = 100

admin.site.register(BindingPhone, BindingPhoneAdmin)


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
	list_display = ('username', 'is_active', 'is_staff', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'get_pin_code')
	
admin.site.unregister(User)
#admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)

