from rest_framework import serializers
from .models import Car, Extra_info

class Extra_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_info
        fields = ['id', 'engine', 'transmission', 'brakes', 'suspension']

class CarSerializer(serializers.ModelSerializer):
    extra_info = Extra_infoSerializer(many=True)
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'color', 'category', 'description', 'year', 'price', 'image', 'extra_info']

