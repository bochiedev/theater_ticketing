from rest_framework.routers import DefaultRouter
from .views import TheaterViewSet, SeatingViewSet

router = DefaultRouter()

router.register('theater', TheaterViewSet, basename='theater')
router.register('seating', SeatingViewSet, basename='seating')


urlpatterns= []
urlpatterns += router.urls