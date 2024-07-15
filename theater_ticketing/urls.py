from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import urls as users_urls

router = DefaultRouter()


urlpatterns = [
    path('api/<str:version>/auth/', include(users_urls)),
]

urlpatterns += router.urls
