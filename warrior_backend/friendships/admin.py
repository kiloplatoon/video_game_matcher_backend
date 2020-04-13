from django.contrib import admin
from django.apps import AppConfig
from friendships.models import Relationship

admin.site.register(Relationship)

class AuthConfig(AppConfig):
    name = 'friendships'