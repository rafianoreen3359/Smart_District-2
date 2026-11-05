from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', lambda request: HttpResponse(
        "Welcome to Library Management API!"
    )),

    path('admin/', admin.site.urls),

    path('api/', include('library.urls')),

    path('api-token-auth/', obtain_auth_token),
]