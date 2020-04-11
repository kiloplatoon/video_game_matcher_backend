from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .forms import RelationshipForm
from .models import Relationship
from .serializers import RelationshipSerializer#, UserCreateSerializer

from accounts.models import User
from accounts.serializers import UserCreateSerializer

@csrf_exempt
def friendship_home(request):
    users = User.objects.all()
    serialized_users = UserCreateSerializer(users).all_users
    return JsonResponse(data=serialized_users, status=200)

@csrf_exempt
def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = UserCreateSerializer(user).user_detail            
            return JsonResponse(data={'Success': 'You have created a new user!', 'user': serialized_user}, status=200)

@csrf_exempt
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    serialized_user = UserCreateSerializer(user).user_detail
    return JsonResponse(data=serialized_user, status=200)

@csrf_exempt
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = UserCreateSerializer(user).user_detail            
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
        if form.is_valid():
            print("WTF")
            relationship = form.save(commit=True)
            serialized_relationship = RelationshipSerializer(relationship).relationship_detail            
            return JsonResponse(data={'Success': 'You have created a new relationship!', 'relationship': serialized_relationship}, status=200)
        else:
            return JsonResponse(data={'Error': 'Relationship already exists or form not valid!'}, status=200)
            
@csrf_exempt
def accept_friend_request(request, action_user, user_id):
    Relationship.objects.filter(user_one=action_user, user_two=user_id).update(status=1, action_user=action_user)# .values()
    user1 = User.objects.get(id=action_user)
    user2 = User.objects.get(id=user_id)
    return JsonResponse(data={f'Success!': f'{user1.username} and {user2.username} are now friends!'}, status=200)


# 0 = Pending 1 = Accepted 2 = Declined 3 = Blocked
@csrf_exempt
def check_friendship(request, action_user, user_id):
    temp = Relationship.objects.filter(Q(user_one=action_user, user_two=user_id) | Q(user_two=action_user, user_one=user_id)).values()
    user1 = User.objects.get(id=action_user)
    user2 = User.objects.get(id=user_id)

    if len(temp) == 0:
        return JsonResponse(data={f'Success!': f'No relation found between {user1.username} and {user2.username}!'})

    status = temp[0]['status']
    action_user_Q = temp[0]['action_user_id']
    if (status == 0 and action_user == action_user_Q):
        return JsonResponse(data={f'Success!': f'{user1.username} has a pending friend request to {user2.username}.'})
    elif (status == 0 and user_id == action_user_Q):
        return JsonResponse(data={f'Success!': f'{user1.username} has a pending friend request from {user2.username}.'})


    elif (status == 1):
        return JsonResponse(data={f'Success!': f'{user1.username} and {user2.username} are friends.'})
    elif (status == 2):
        return JsonResponse(data={f'Success!': f'{user2.username} has declined {user2.username} friend request.'})
    elif (status == 3):
        return JsonResponse(data={f'Success!': f'{user2.username} has blocked {user2.username}.'})

@csrf_exempt
def friends_list(request, action_user):
    temp = Relationship.objects.filter(Q(user_one=action_user, status=1) | Q(user_two=action_user, status=1) ).values()
    print(len(temp))
    print(temp)
    list = []
    user1 = User.objects.get(id=action_user)
    for i in temp:
        if user1.username != User.objects.get(id = i['user_two_id']).username:
            list.append(User.objects.get(id = i['user_two_id']).username)

        if user1.username != User.objects.get(id = i['user_one_id']).username:
            list.append(User.objects.get(id = i['user_one_id']).username)

    user1 = User.objects.get(id=action_user)
    return JsonResponse(data={f'Success!': f'{user1.username} friend list: {list}'})

@csrf_exempt
def pending_requests(request, action_user):
    temp = Relationship.objects.filter(user_two=action_user, status=0).values()

    list = []
    for i in temp:
        list.append(User.objects.get(id = i['user_on_id']).username)

    user1 = User.objects.get(id=action_user)
    return JsonResponse(data={f'Success!': f'{user1.username} pending friend request list: {list}'})

@csrf_exempt
def friend_requests_sent_by_user(request, action_user):

    temp = Relationship.objects.filter(user_one=action_user, status=0).values()

    list = []
    for i in temp:
        list.append(User.objects.get(id = i['user_two_id']).username)

    user1 = User.objects.get(id=action_user)
    return JsonResponse(data={f'Success!': f'{user1.username} pending sent friend request list: {list}'})




    # temp = Relationship.objects.filter(user_one=action_user, status=0).values()

    # list = []
    # for i in temp:
    #     list.append(User.objects.get(id = i['user_two_id']).username)

    # user1 = User.objects.get(id=action_user)
    # return JsonResponse(data={f'Success!': f'{user1.username} pending friend request list: {list}'})