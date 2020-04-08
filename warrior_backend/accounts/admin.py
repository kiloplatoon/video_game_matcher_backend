from django.contrib import admin
from django.apps import AppConfig
from accounts.models import User

admin.site.register(User)

class AuthConfig(AppConfig):
    name = 'accounts'