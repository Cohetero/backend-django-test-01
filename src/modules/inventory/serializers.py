from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=50)
    unit_price = serializers.IntegerField()
    stock = serializers.IntegerField()
    
    class Meta:
        model = Product
        fields = ('__all__')