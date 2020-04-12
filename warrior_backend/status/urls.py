from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_status),
    path('<int:user_id>/create/', views.create_status),
    path('<int:status_id>/edit/', views.edit_status),
    path('<int:status_id>/delete/', views.delete_status)
]