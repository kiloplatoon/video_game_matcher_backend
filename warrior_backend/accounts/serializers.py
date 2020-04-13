from djoser.serializers import UserCreateSerializer, UserSerializer, TokenSerializer
from djoser.conf import settings as djoser_settings
from stream_chat import StreamChat
from django.conf import settings
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name')

    @property
    def all_users(self):
        output = {'users': []}
        for user in self.user_body:
            user_details = {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'password': user.password,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            output['users'].append(user_details)
        return output

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
        token = client.create_token(obj.user.username)

        return token

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'profile_picture',
            'bio',
            'dob',
            'casual_competitive',
            'platform',
            'game',
        )