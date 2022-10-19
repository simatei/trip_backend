from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Trip
from .serializers import TripSerializer, TripCreationSerializer


class TripView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Gets all trips from db and return them
        :param request:
        :return:
        """
        trips_qs = Trip.objects.all()
        serializer = TripSerializer(trips_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = {
                "address_type": request.data.get("address_type"),
                "driver_id": request.data.get("driver_id"),
                "vehicle_id": request.data.get("vehicle_id"),
                "customer_id": request.data.get("customer_id"),
                "address": request.data.get("address"),
                "cargo_tonnage": request.data.get("cargo_tonnage"),
            }

            valid_address_types = ["pick_up_point", "drop_off_point"]
            if data["address_type"] not in valid_address_types:
                return Response(
                    {"error": "Invalid address type"}, status=status.HTTP_400_BAD_REQUEST
                )

            serializer = TripCreationSerializer(data=data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "status": status.HTTP_201_CREATED,
                    "description": "Trip created successfully",
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "description": "Something went wrong",
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

