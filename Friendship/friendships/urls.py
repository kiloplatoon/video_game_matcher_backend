from django.urls import path
from . import views

urlpatterns = [
    path('', views.friendship_home, name='friendship_home'),
    path('new_user', views.new_user, name='new_user'),
    path('<int:user_id>', views.user_detail, name='user_detail'),
    path('<int:user_id>/edit', views.edit_user, name='edit_user'),
    path('<int:user_id>/delete', views.delete_user, name='delete_user'),

    path('relationship', views.relationship_detail, name='relationship_detail'),
    path('relationship/friend_request', views.friend_request, name='friend_request'),

    #                  action user = who is accepting           user_id = who is being accepted by action user
    path('relationship/<int:action_user>/accept_friend_request/<int:user_id>', views.accept_friend_request, name='accept_friend_request'),

    path('relationship/<int:action_id>/check_friendship/<int:user_id>', views.check_friendship, name='check_friendship'),
    path('relationship/<int:action_id>/friends_list', views.friends_list, name='friends_list'),
    path('relationship/<int:action_id>/pending_requests', views.pending_requests, name='pending_requests'),
    path('relationship/<int:action_id>/friend_requests_sent_by_user', views.friend_requests_sent_by_user, name='friend_requests_sent_by_user'),

]