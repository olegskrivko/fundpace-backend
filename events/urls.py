from django.urls import path
from .views import EventsHomeView

urlpatterns = [
    # Resulting URL: /api/v1/events/
    path('events/', EventsHomeView.as_view(), name='events-home'),
]