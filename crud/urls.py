from django.urls import path
from .views import AllProduct,CarPage,CarDetailPage,CarDetailEditPage,CarDetailDeletePage,CarCreatePage, Categories, Savatcha, CategorCreatePage ,AddCardPage,SearchPage,ItemDelete


urlpatterns = [
    path('', Categories, name = 'homepage'),
    path('allproduct/', AllProduct, name='allproduct'),
    path('createcategor/', CategorCreatePage, name = 'createcategor'),
    path('<slug:category>', CarPage, name = 'carpage'),
    path('search/', SearchPage, name='search'),
    path('savat/', Savatcha,  name = 'savatcha'),
    path('savat/<int:pk>', ItemDelete, name='itemdelete'),
    path('Car/create/', CarCreatePage, name = 'create'),
    path('Car/detail/<int:pk>', CarDetailPage, name = 'detail'),
    path('<slug:category>/add/<int:pk>', AddCardPage, name = 'add_card'),
    path('Car/detail/<int:pk>/edit', CarDetailEditPage, name = 'edit'),
    path('Car/detail/<int:pk>/delete', CarDetailDeletePage, name='delete'),
]