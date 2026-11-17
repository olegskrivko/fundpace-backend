from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountsTests(APITestCase):
    """
    Test suite for accounts app endpoints.
    """

    def test_accounts_home_success(self):
        url = reverse("accounts-home")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello from Accounts API!")