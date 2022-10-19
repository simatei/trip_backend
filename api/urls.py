from django.urls import path
from .views import TripView

urlpatterns = [
    path("trips", TripView.as_view(), name="trip-logs"),
    path("trips/create/api_token=<str:api_token>", TripView.as_view(), name="trips-create"),

]