from rest_framework import viewsets
from users.permissions import IsVerifiedBrandOrReadOnly
from .models import Campaign
from .serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = (
        Campaign.objects.select_related("event", "brand")
        .prefetch_related("slots__race")
        .all()
    )
    serializer_class = CampaignSerializer
    permission_classes = [IsVerifiedBrandOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()

        event_id = self.request.query_params.get("event")
        if event_id:
            queryset = queryset.filter(event_id=event_id)

        status_param = self.request.query_params.get("status")
        if status_param:
            queryset = queryset.filter(status=status_param)

        return queryset

    def perform_create(self, serializer):
        serializer.save(brand=self.request.user)