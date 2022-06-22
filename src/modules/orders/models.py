from django.db import models
from modules.inventory.models import Product

class Order(models.Model):
    total = models.PositiveIntegerField()

class Item(models.Model):
    quantity = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)