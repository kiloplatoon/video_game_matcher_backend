from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('profile/', include('accounts.urls')),
    path('friendships/', include('friendships.urls')),
    path('status/', include('status.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
