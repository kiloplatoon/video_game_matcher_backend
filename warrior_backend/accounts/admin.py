from django.contrib import admin
from django.apps import AppConfig
from accounts.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)

class AuthConfig(AppConfig):
    name = 'accounts'