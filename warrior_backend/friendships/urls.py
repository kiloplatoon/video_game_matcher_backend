from django.urls import path
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.friendship_home, name='friendship_home'),
    path('new_user', views.new_user, name='new_user'),
    path('<int:user_id>', accounts_views.current_user, name='user_detail'),
    path('<int:user_id>/edit', views.edit_user, name='edit_user'), # probably can delete
    path('<int:user_id>/delete', views.delete_user, name='delete_user'), # probably can delete

    path('relationship', views.relationship_detail, name='relationship_detail'),
    path('relationship/friend_request', views.friend_request, name='friend_request'),

    #                  action user = who is accepting           user_id = who is being accepted by action user
    path('relationship/<int:action_user>/accept_friend_request/<int:user_id>', views.accept_friend_request, name='accept_friend_request'),

    path('relationship/<int:action_user>/check_friendship/<int:user_id>', views.check_friendship, name='check_friendship'), 
    path('relationship/<int:action_user>/friends_list', views.friends_list, name='friends_list'),
    path('relationship/<int:action_user>/pending_requests', views.pending_requests, name='pending_requests'),
    path('relationship/<int:action_user>/friend_requests_sent_by_user', views.friend_requests_sent_by_user, name='friend_requests_sent_by_user'),

]