from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


from friendships import views
from friendships.models import Relationship

# Create your views here.
@api_view(['GET'])
def current_user(request, user_id):
    """
    Determine the current user by their token, and return their data
    """

    user = User.objects.values().get(id=user_id)
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data) and render(request, 'current_user.html', {'user' : user})
