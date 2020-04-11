from django.shortcuts import render
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerialzier
from .models import User, Profile
from django.http import JsonResponse
import json
from .forms import ProfileForm

def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerialzier(profiles, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def link(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile(user=user)
    serializer = ProfileSerialzier(profile, many=False)
    return Response(serializer.data)

def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    serialized_profile = ProfileSerializer(profile)
    return JsonResponse(data=serialized_profile, status=200)

def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    data = json.loads(request.body)
    if request.method == "POST":
        form = ProfileForm(data, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            serialized_profile = ProfileSerializer(profile)
            return JsonResponse(data=serialized_profile, status=200)



# Create your views here.
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
