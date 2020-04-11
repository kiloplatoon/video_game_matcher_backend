from django.shortcuts import render
from . import models, serializers

from django.http import JsonResponse

def profile_detail(request, profile_id):
    profile = profile.objects.get(id=profile_id)
    serialized_profile = ProfileSerializer(profile).profile_detail
    return JsonResponse(data=serialized_profile, status=200)

def edit_profile(request, profile_id):
    profile = profile.objects.get(id=profile_id)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=True)
            serialized_profile = ProfileSerializer(profile).profile_detail
            return JsonResponse(data=serialized_profile, status=200)