from django.db import models
from theater_ticketing.models import BaseModel
from theaters.models import Seating
from users.models import User

# Create your models here.


class Reservation(BaseModel):
    seating = models.ForeignKey(Seating, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('seating', 'seat_number')

    def __str__(self):
        return f"Reservation for {self.user.get_full_name()} at {self.seating} seat {self.seat_number}"
