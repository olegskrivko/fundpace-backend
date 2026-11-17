import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_events_home_success():
    client = APIClient()
    url = reverse("events-home")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Hello from Events API!"


@pytest.mark.django_db
def test_events_list_empty():
    """
    Test that getting events list returns an empty list initially.
    """
    client = APIClient()
    url = reverse("events-home")  # Vēlāk nomainīsim uz reālu list URL
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    # Pagaidām pārbaudām mūsu Hello World ziņu, vēlāk šeit būs list dati
    assert "message" in response.data