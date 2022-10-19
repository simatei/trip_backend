from django.urls import path
from .views import TripView

urlpatterns = [
    path("trips", TripView.as_view(), name="trips"),
]