from django.urls import path
from .views import CampaignsHomeView

urlpatterns = [
    # Resulting URL: /api/v1/campaigns/
    path("campaigns/", CampaignsHomeView.as_view(), name="campaigns-home"),
]
