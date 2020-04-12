from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('<int:user_id>/', views.link),
    path('list/', views.profile_list),
    path('<int:user_id>/edit/', views.edit_profile, name='profile'),
    path('<int:user_id>/details/', views.profile_detail),
    
    
    path('current_user/', views.current_user),
]