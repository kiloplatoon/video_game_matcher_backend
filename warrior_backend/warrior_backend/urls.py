from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('profile/', include('accounts.urls')),
    path('friendships/', include('friendships.urls')),
    path('status/', include('status.urls')),
]
