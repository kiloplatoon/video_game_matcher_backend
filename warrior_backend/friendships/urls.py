from django.urls import path
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.friendship_home, name='friendship_home'),
    path('new_user', views.new_user, name='new_user'),
    path('<int:user_id>', accounts_views.current_user, name='user_detail'),
    path('<int:user_id>/edit', views.edit_user, name='edit_user'), # probably can delete
    path('<int:user_id>/delete', views.delete_user, name='delete_user'), # probably can delete

    path('<int:user_id>/view_profile/<int:target_user>', views.view_profile, name='view_profile'),

    path('<int:user_id>/friends_list', views.go_to_friends_list, name='go_to_friends_list'),

    path('<int:user_id>/search_results', views.search_results, name='search_results'),

    path('<int:user_id>/received_friend_requests', views.received_friend_requests, name='received_friend_requests'),

    path('<int:user_id>/sent_friend_requests', views.sent_friend_requests, name='sent_friend_requests'),

    path('<int:user_id>/accept_friend_request/<int:action_user>', views.accept_friend_request, name='accept_friend_request'),

    path('<int:user_id>/deny_friend_request/<int:action_user>', views.deny_friend_request, name='deny_friend_request'),

    path('<int:user_id>/delete_friend/<int:action_user>', views.deny_friend_request, name='deny_friend_request'),

    path('relationship', views.relationship_detail, name='relationship_detail'),
    path('relationship/friend_request', views.friend_request, name='friend_request'),

    #                  action user = who is accepting           user_id = who is being accepted by action user
    path('relationship/<int:action_user>/accept_friend_request/<int:user_id>', views.accept_friend_request, name='accept_friend_request'),

    path('relationship/<int:action_user>/check_friendship/<int:user_id>', views.check_friendship, name='check_friendship'), 
    path('relationship/<int:action_user>/friends_list', views.friends_list, name='friends_list'),
    path('relationship/<int:action_user>/pending_requests', views.pending_requests, name='pending_requests'),
    path('relationship/<int:action_user>/friend_requests_sent_by_user', views.friend_requests_sent_by_user, name='friend_requests_sent_by_user'),

]