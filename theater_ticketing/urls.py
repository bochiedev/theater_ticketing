from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from users import urls as user_urls
from theaters import urls as theater_urls
from reservations import urls as reservation_urls



router = DefaultRouter()


urlpatterns = [
    path('api/<str:version>/', include(router.urls)),
    path('api/<str:version>/auth/', include(user_urls)),
    path('api/<str:version>/', include(theater_urls)),
    path('api/<str:version>/', include(reservation_urls)),


]

urlpatterns += router.urls
