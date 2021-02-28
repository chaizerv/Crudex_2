from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/oneapp/', include('oneapp.urls')),
    path('api/v1/auth_token/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]

