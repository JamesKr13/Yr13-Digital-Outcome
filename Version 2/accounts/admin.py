from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     model = User
#     list_display = ('username', 'email', 'access_group', 'delete_on', 'api_key')
#     list_filter = ('username', 'email', 'access_group', 'is_superuser', 'delete_on')
#     readonly_fields = ['date_joined', 'api_key', 'last_login']
#     fieldsets = (
#         ('User', {'fields': ('username', 'email', 'password', 'access_group')}),
#         ('Permissions', {'fields': (('is_staff', 'is_active'), 'access_group', 'delete_on')}),
#         )
#     add_field_sets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', ('password1', 'password2'))
#             }),
#         ('Permissions', {'fields': (('is_staff', 'is_active'), 'access_group', 'delete_on')})
#         )
#     search_fields = ('username', 'email', 'first_name', 'last_name', 'account_name', 'access_group', 'delete_on')
#     ordering = ('username', 'email', 'first_name', 'last_name', 'access_group', 'account_name', 'delete_on')
# class CustomUserAdmin(UserAdmin):
#     list_display = (
#         'username', 'email', 'first_name', 'last_name',
#         'club'
#         )

#     fieldsets = (
#         (None, {
#             'fields': ('username', 'password')
#         }),
#         ('Personal info', {
#             'fields': ('first_name', 'last_name', 'email')
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active',
#                 )
#         }),
#         ('Important dates', {
#             'fields': ('last_login', 'date_joined')
#         }),
#         ('Additional info', {
#             'fields': ('email', 'club')
#         })
#     )

#     add_fieldsets = (
#         (None, {
#             'fields': ('username', 'password1', 'password2')
#         }),
#         ('Personal info', {
#             'fields': ('first_name', 'last_name', 'email')
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active'
#                 )
#         }),
#         ('Important dates', {
#             'fields': ('last_login', 'date_joined')
#         }),
#         ('Additional info', {
#             'fields': ('club', 'email')
#         })
#     )

admin.site.register(CustomUser)