from django.db import models
from .Category import Categor
class Car(models.Model):
    name = models.CharField(max_length=25, blank=True)
    color = models.CharField(max_length=15, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Categor, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name