from rest_framework import serializers
from reservations.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['uid', 'seating', 'user', 'seat_number']
