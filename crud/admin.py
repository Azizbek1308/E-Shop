from django.contrib import admin
from .models.Products import Car
from .models.Category import Categor
from .models.savat import Savat

# Register your models here.

admin.site.register(Car)
admin.site.register(Categor)
admin.site.register(Savat)


