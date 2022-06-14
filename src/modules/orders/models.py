from statistics import mode
from django.db import models

class Order(models.Model):
    total = models.PositiveIntegerField()
