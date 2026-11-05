from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


def home(request):
    return render(request, 'home.html')


urlpatterns = [

    path('', home, name='home'),

    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),

    path('api/', include('assignments.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/docs/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),

    path('api/redoc/', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]