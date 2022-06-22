from rest_framework import serializers
from .models import Order, Item
from modules.inventory.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('__all__')

class ItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    total = serializers.IntegerField()
    id_product = ProductSerializer()
    id_order = OrderSerializer()

    class Meta:
        model = Item
        fields = ('__all__')