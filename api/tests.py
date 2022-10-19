from django.test import TestCase
from rest_framework.test import APIClient, force_authenticate, APIRequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class TestTrip(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("trips")

    def test_trip_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    # def test_trip_creation(self):
    #     data = {
    #         "pick_up": "The Address",
    #         "drop_off": "Some Other Place",
    #         "driver_id": 1,
    #         "customer_id": 3,
    #         "tonnage": 203,
    #     }

    #     response = self.client.post(self.url, data=data)
    #     self.assertEqual(response.status_code, 201)