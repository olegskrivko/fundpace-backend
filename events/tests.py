# events/tests/test_views.py
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.urls import reverse
import pytest
from rest_framework import status
from rest_framework.test import APIClient

from events.models import Event, Race

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def regular_user(db):
    return User.objects.create_user(username="runner", password="password123", is_staff=False)


@pytest.fixture
def staff_user(db):
    return User.objects.create_user(username="admin_staff", password="password123", is_staff=True)


@pytest.fixture
def sample_event(db):
    return Event.objects.create(
        name="Rimi Riga Marathon",
        location="Riga",
        start_date="2027-05-15",
        end_date="2027-05-16",
        description="The biggest marathon in the Baltics.",
    )


@pytest.fixture
def sample_race(db, sample_event):
    return Race.objects.create(
        event=sample_event,
        name="Half Marathon",
        distance_km=Decimal("21.0975"),
        race_date="2027-05-16",
        start_time="09:00:00",
    )


@pytest.mark.django_db
class TestEventEndpoints:
    def test_list_events_public(self, api_client, sample_event, sample_race):
        url = "/api/v1/events/"
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == sample_event.name
        # Verify nested races serializer is working
        assert len(response.data[0]["races"]) == 1
        assert response.data[0]["races"][0]["name"] == sample_race.name

    def test_create_event_unauthenticated_forbidden(self, api_client):
        url = "/api/v1/events/"
        payload = {
            "name": "Sigulda Trail",
            "location": "Sigulda",
            "start_date": "2027-09-06",
            "end_date": "2027-09-06",
        }
        response = api_client.post(url, payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_event_regular_user_forbidden(self, api_client, regular_user):
        api_client.force_authenticate(user=regular_user)
        url = "/api/v1/events/"
        payload = {
            "name": "Sigulda Trail",
            "location": "Sigulda",
            "start_date": "2027-09-06",
            "end_date": "2027-09-06",
        }
        response = api_client.post(url, payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_event_staff_success(self, api_client, staff_user):
        api_client.force_authenticate(user=staff_user)
        url = "/api/v1/events/"
        payload = {
            "name": "Sigulda Trail",
            "location": "Sigulda",
            "start_date": "2027-09-06",
            "end_date": "2027-09-06",
            "description": "Gravel race",
        }
        response = api_client.post(url, payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert Event.objects.filter(name="Sigulda Trail").exists()


@pytest.mark.django_db
class TestRaceEndpoints:
    def test_filter_races_by_event(self, api_client, sample_event, sample_race):
        # Create another event and race to test filtering
        other_event = Event.objects.create(
            name="Tallinn Marathon", location="Tallinn", start_date="2027-09-12", end_date="2027-09-13"
        )
        Race.objects.create(
            event=other_event, name="10K", distance_km=Decimal("10.0000"), race_date="2027-09-12"
        )

        url = f"/api/v1/races/?event={sample_event.id}"
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["id"] == sample_race.id

    def test_race_date_bounds_validation(self, api_client, staff_user, sample_event):
        api_client.force_authenticate(user=staff_user)
        url = "/api/v1/races/"
        
        # Race date is outside event start/end (event is May 15-16, race is May 20)
        payload = {
            "event": sample_event.id,
            "name": "Out of Bounds Race",
            "distance_km": "5.0000",
            "race_date": "2027-05-20",
        }
        response = api_client.post(url, payload)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "race_date" in response.data