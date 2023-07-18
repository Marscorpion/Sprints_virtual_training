from django.urls import include, path
from rest_framework import routers
from . import views
from .views import CoordinateViewSet, ImageViewSet, UserViewSet, PassViewSet

router = routers.DefaultRouter()
router.register(r'coordinates', CoordinateViewSet)
router.register(r'images', ImageViewSet)
router.register(r'users', UserViewSet)
router.register(r'passes', PassViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/submit-data/', views.submitData, name='submit-data'),
]