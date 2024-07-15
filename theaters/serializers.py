
from rest_framework import serializers
from theaters.models import Seating, Theater

class SeatingSerializer(serializers.ModelSerializer):
    available_seats = serializers.SerializerMethodField()
    booked_seats = serializers.SerializerMethodField()
    theater = serializers.SerializerMethodField()


    class Meta:
        model = Seating
        fields = ['uid', 'title', 'theater', 'show_date', 'available_seats', 'booked_seats']

    def get_available_seats(self, obj):
        booked_seats = obj.reservation_set.values_list('seat_number', flat=True)
        return list(set(range(1, obj.theater.total_seats + 1)) - set(booked_seats))

    def get_booked_seats(self, obj):
        return obj.reservation_set.values_list('seat_number', flat=True)
    
    def get_theater(self, obj):
        return obj.theater.name


class TheaterSerializer(serializers.ModelSerializer):
    seatings = serializers.SerializerMethodField()


    class Meta:
        model = Theater
        fields = ['uid', 'name', 'total_seats', 'seatings']

    def get_seatings(self, obj):
        seatings = obj.seatings.all()
        return SeatingSerializer(seatings, many=True).data

