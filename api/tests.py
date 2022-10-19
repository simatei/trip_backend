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
        self.token = Token.objects.create(user=self.user)

    def test_get_trip_logs(self):
        # Test that we can get a log of the trip
        response = self.client.get(reverse("trips-log"))
        self.assertEqual(response.status_code, 200)

    # def test_trip_creation(self):
    #     # Test that a trip can be created"""
    #     data = {
    #         "address_type": "pick_up_point",
    #         "driver_id": 3,
    #         "vehicle_id": 4,
    #         "customer_id": 2,
    #         "address": "adress",
    #         "cargo_tonnage": 100.34,
    #     }


    #     response = self.client.post(reverse("trips-create"), data=data, kwargs={"api_token": self.token})
    #     self.assertEqual(response.status_code, 201)
