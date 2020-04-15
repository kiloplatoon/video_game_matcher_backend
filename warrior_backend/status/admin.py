from django.contrib import admin
from django.apps import AppConfig
from status.models import Status

admin.site.register(Status)

class AuthConfig(AppConfig):
    name = 'status'