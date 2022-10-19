from rest_framework import serializers
from .models import Trip
from django.contrib.auth import get_user_model

User = get_user_model()


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class TripCreationSerializer(serializers.Serializer):

    address_type = serializers.CharField(max_length=20)
    driver_id = serializers.IntegerField()
    vehicle_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()
    address = serializers.CharField(max_length=50)
    cargo_tonnage = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        done_by_user_id = self.context["request"].user.id
        user = User.objects.get(id=done_by_user_id)
        data = {
            "address_type": validated_data.get("address_type"),
            "driver_id": validated_data.get("driver_id"),
            "vehicle_id": validated_data.get("vehicle_id"),
            "customer_id": validated_data.get("customer_id"),
            "address": validated_data.get("address"),
            "cargo_tonnage": validated_data.get("cargo_tonnage"),
            "done_by": user
        }

        return Trip.objects.create(**data)
