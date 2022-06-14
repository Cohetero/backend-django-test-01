from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Order
from modules.inventory.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True)
    total = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('__all__')