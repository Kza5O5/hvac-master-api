from rest_framework import serializers
from .models import Car, Blog, Service


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'year',
            'image',
            'price',
            'stock',
            'vin',
            'mile',
            'tranmission',
            'housepw'
        ]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = 'all'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = 'all'