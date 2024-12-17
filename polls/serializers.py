from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Clothes

class ClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'