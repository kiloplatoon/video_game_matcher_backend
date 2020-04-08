from django.contrib import admin
from django.apps import AppConfig
from 


admin.site.register(User)

class AuthConfig(AppConfig):
    name = 'accounts'