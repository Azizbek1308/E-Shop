from django.forms import ModelForm
from .models.Products import Car
from .models.savat import Savat
from .models.Category import Categor

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name','color','date','image', 'category','price']

class CategorForm(ModelForm):
    class Meta:
        model = Categor
        fields = ['name']

class SavatForm(ModelForm):
    class Meta:
        model = Savat
        fields = ['name','price','count']

class CarsavatForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name']

