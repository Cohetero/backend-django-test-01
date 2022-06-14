from django.db import models
from modules.orders.models import Order

class Product(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    total = models.PositiveIntegerField(default=0)
    orde = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, blank=True)

