from rest_framework import viewsets
from users.permissions import IsAdminOrStaffOrReadOnly
from .models import Event, Race
from .serializers import EventSerializer, RaceSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.prefetch_related("races").all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.select_related("event").all()
    serializer_class = RaceSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.request.query_params.get("event")
        if event_id:
            queryset = queryset.filter(event_id=event_id)
        return queryset