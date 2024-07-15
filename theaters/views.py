from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Theater, Seating
from .serializers import TheaterSerializer, SeatingSerializer

# Create your views here.
class TheaterViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        theaters = Theater.objects.all()
        serializer = TheaterSerializer(theaters, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            theater = Theater.objects.get(pk=pk)
            serializer = TheaterSerializer(theater)
            return Response(serializer.data)
        except Theater.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            theater = Theater.objects.get(pk=pk)
            serializer = TheaterSerializer(theater, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Theater.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            theater = Theater.objects.get(pk=pk)
            theater.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Theater.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SeatingViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        seatings = Seating.objects.all()
        serializer = SeatingSerializer(seatings, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = SeatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            seating = Seating.objects.get(pk=pk)
            serializer = SeatingSerializer(seating)
            return Response(serializer.data)
        except Seating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            seating = Seating.objects.get(pk=pk)
            serializer = SeatingSerializer(seating, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Seating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            seating = Seating.objects.get(pk=pk)
            seating.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Seating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)