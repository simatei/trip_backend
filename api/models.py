from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Trip(models.Model):
    PICK_UP_POINT, DROP_OFF_POINT = "PICK_UP_POINT", "DROP_OFF_POINT"
    POINT_TYPE_CHOICES = (
        (PICK_UP_POINT, "pick_up_point"),
        (DROP_OFF_POINT, "drop_off_point"),
    )
    address_type = models.CharField(max_length=20, choices=POINT_TYPE_CHOICES)
    driver_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    customer_id = models.IntegerField()
    address = models.CharField(max_length=50)
    cargo_tonnage = models.DecimalField(max_digits=10, decimal_places=2)
    done_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.address_type, self.cargo_tonnage)
