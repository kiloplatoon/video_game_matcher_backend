from django.shortcuts import render
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile
from django.http import JsonResponse
import json
from .forms import ProfileForm

@api_view(('GET',))
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def link(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile(user=user).save()
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(('GET',))
def profile_detail(request, user_id):
    user = User.objects.get(id=user_id)
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return JsonResponse(data=serialized_profile.data, status=200, safe = False)

@api_view(('POST',))
def edit_profile(request, user_id):
    user1 = User.objects.get(id=user_id)
    profile = Profile.objects.get(user = user1)
    data = json.loads(request.body)
    if request.method == "POST":
        form = ProfileForm(data, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            serialized_profile = ProfileSerializer(profile)
            return JsonResponse(data=serialized_profile.data, safe = False)



# Create your views here.
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
