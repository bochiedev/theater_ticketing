from django.db import models
from theater_ticketing.models import BaseModel


# Create your models here.

class Theater(BaseModel):
    name = models.CharField(max_length=100)
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Seating(BaseModel):
    title = models.CharField(max_length=100)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    show_date = models.DateField()

    def __str__(self):
        return f"{self.theater.name} on {self.show_date}"