from django.db import  models
from .Products import Car

class Savat(models.Model):
    name = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField(default=1)