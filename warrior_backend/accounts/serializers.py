from djoser.serializers import UserCreateSerializer, UserSerializer, TokenSerializer
from djoser.conf import settings as djoser_settings
from stream_chat import StreamChat
from django.conf import settings
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email','username','password','first_name','last_name')

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email','username',
        )

class StreamTokenSerializer(TokenSerializer):
    stream_token = serializers.SerializerMethodField()

    class Meta:
        model = djoser_settings.TOKEN_MODEL
        fields = ('auth_token','stream_token')

    def get_stream_token(self, obj):
        client = StreamChat(api_key=settings.STREAM_API_KEY, api_secret=settings.STREAM_API_SECRET)
        token = client.create_token(obj.user.email)

        return token