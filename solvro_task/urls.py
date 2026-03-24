from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # To już masz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('api/cocktails/', permanent=False)),
    path('api/', include('cocktails.urls')),
    path('api/auth/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')), #doda logowanie!!!
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)