from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Trip
from .serializers import TripSerializer
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
        """
        Creates a new trip
        :param request:
        :return:
        """
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
