from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MotoImageViewSet

router = DefaultRouter()


router.register(r"moto-images", MotoImageViewSet, basename="motoimage")

urlpatterns = [
    path("", include(router.urls)),
]
