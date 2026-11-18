from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CampaignsTests(APITestCase):
    """
    Test suite for campaigns app endpoints.
    """

    def test_campaigns_home_success(self):
        url = reverse("campaigns-home")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello from Campaigns API!")
