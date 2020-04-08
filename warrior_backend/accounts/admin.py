from django.contrib import admin
from django.apps import AppConfig

admin.site.register(User)

class AuthConfig(AppConfig):
    name = 'accounts'