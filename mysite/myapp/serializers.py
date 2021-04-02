from .models import *
from rest_framework import serializers

class ManufacturerSerializer(serializers.ModelSerializer):
    cars = serializers.StringRelatedField(many=True)

    class Meta:
        model = Manufacturer
        fields = ['name', 'cars']


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    class Meta:
        model = Car
        fields = ['name', 'manufacturer']
#
# class ManufacturerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Manufacturer
#         fields = ['name', 'cars']
#
#
# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = ['name', 'manufacturer']
