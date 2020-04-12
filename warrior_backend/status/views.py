from django.http import JsonResponse
from django.shortcuts import render
from accounts.models import User
from .models import Status
from .forms import StatusForm
from .serializer import StatusSerializer
from django.views.decorators.csrf import csrf_exempt
import json


def list_status(request):
    statuses = Status.objects.all()
    serializer = StatusSerializer(statuses, many=True)
    return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def create_status(request, user_id):
    user = User.objects.get(id=user_id)
    data = json.loads(request.body)
    if request.method == 'POST':
        form = StatusForm(data)
        if form.is_valid():
            status = form.save(commit=False)
            status.user = user
            status.save()
            serializer = StatusSerializer(status)
            return JsonResponse(data = serializer.data, safe = False)

@csrf_exempt
def edit_status(request, status_id):
    status = Status.objects.get(id=status_id)
    data = json.loads(request.body)
    if request.method == "POST":
        form = StatusForm(data, instance=status)
        if form.is_valid():
            status = form.save(commit=True)
            status.save()
            serialized_status = StatusSerializer(status)
            return JsonResponse(data=serialized_status.data, status=200, safe = False)

@csrf_exempt
def delete_status(request, status_id):
    if request.method == "POST":
        status = Status.objects.get(id=status_id)
        status.delete()
        return JsonResponse(data={'status': 'Status Deleted.'}, status=200, safe = False)
