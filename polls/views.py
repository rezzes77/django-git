from rest_framework import viewsets
from .models import Clothes
from .models import Car
from .serializers import ClothesSerializers
from .serializers import CarSerializers
class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers