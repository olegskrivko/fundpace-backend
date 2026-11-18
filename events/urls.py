from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RaceViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")
router.register(r"races", RaceViewSet, basename="race")

urlpatterns = [
    path("", include(router.urls)),
]
