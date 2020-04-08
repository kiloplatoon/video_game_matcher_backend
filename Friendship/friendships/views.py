from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm, RelationshipForm
from .models import User, Relationship
from .serializers import RelationshipSerializer, UserSerializer

@csrf_exempt
def friendship_home(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users).all_users
    return JsonResponse(data=serialized_users, status=200)

@csrf_exempt
def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = UserSerializer(user).user_detail            
            return JsonResponse(data={'Success': 'You have created a new user!', 'user': serialized_user}, status=200)

@csrf_exempt
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    serialized_user = UserSerializer(user).user_detail
    return JsonResponse(data=serialized_user, status=200)

@csrf_exempt
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = UserSerializer(user).user_detail            
            return JsonResponse(data={'Success': 'You have edited a user!', 'user': serialized_user}, status=200)

@csrf_exempt
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return JsonResponse(data={'Success': 'You have deleted a user!'}, status=200)

@csrf_exempt
def relationship_detail(request):
    relationships = Relationship.objects.all()
    serialized_relationships = RelationshipSerializer(relationships).all_relationships
    return JsonResponse(data=serialized_relationships, status=200)

@csrf_exempt
def friend_request(request):
    if request.method == 'POST':
        form = RelationshipForm(request.POST)
        print(form)
        if form.is_valid():
            print("WTFFF")
            relationship = form.save(commit=True)
            serialized_relationship = RelationshipSerializer(relationship).relationship_detail            
            return JsonResponse(data={'Success': 'You have created a new relationship!', 'relationship': serialized_relationship}, status=200)

@csrf_exempt
def accept_friend_request(request, action_user, user_id):
    Relationship.objects.filter(user_one=action_user, user_two=user_id).update(status=1, action_user=action_user)# .values()
    user1 = User.objects.get(id=action_user)
    user2 = User.objects.get(id=user_id)
    return JsonResponse(data={f'Success!': f'{user1.username} and {user2.username} are now friends!'}, status=200)
    # print(temp)
    # print(action_user, user_id)
    pass

# 0 = Pending 1 = Accepted 2 = Declined 3 = Blocked
@csrf_exempt
def check_friendship(request, action_user, user_id):
    pass

@csrf_exempt
def friends_list(request, action_user):
    pass
    # relationship = Relationship.objects.get(id=relationship_id)
    # serialized_relationship = RelationshipSerializer(relationship).relationship_detail
    # return JsonResponse(data=serialized_relationship, status=200)

@csrf_exempt
def pending_requests(request, action_user):
    pass

@csrf_exempt
def friend_requests_sent_by_user(request, action_user):
    pass