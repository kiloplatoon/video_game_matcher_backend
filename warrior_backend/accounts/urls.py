from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('<int:user_id>/', views.link),
    path('list/', views.profile_list),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile'),
    
    
    path('current_user/', views.current_user),
]