from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Seating, Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        user = request.user
        reservations = Reservation.objects.filter(user=user)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = str(request.user.uid)

        try:
            seating = Seating.objects.get(uid=data['seating'])
        except Seating.DoesNotExist:
            return Response({"error": "Seating does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        seat_number = int(data['seat_number'])

        if seat_number < 1 or seat_number > seating.theater.total_seats:
            return Response({"error": "Seat number out of range"}, status=status.HTTP_400_BAD_REQUEST)

        if Reservation.objects.filter(seating=seating, seat_number=seat_number).exists():
            return Response({"error": "Seat already booked"}, status=status.HTTP_400_BAD_REQUEST)
        
        print("DATA", data)

        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk)
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk)
            serializer = ReservationSerializer(reservation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk)
            reservation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)