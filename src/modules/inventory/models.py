from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=50)
    unit_price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()