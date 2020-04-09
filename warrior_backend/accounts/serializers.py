from djoser.serializers import UserCreateSerializer, UserCreateSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email','username','password','first_name','last_name')


class ProfileSerialzier(ProfileSerialzier):
    class Meta(ProfileSerialzier.Meta):
        Model = Profile
        field = ('username', 'bio', 'dob', 'profile_picture')