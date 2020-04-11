from djoser.serializers import UserCreateSerializer, UserCreateSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email','username','password','first_name','last_name')


class ProfileSerialzier(serializers.ModelSerializer):
    user = User()
    class Meta:
        model = Profile
        fields = (
            'user',
            
        )