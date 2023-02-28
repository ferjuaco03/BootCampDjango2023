from django.urls import path
from ProductApp.views import products, Orders, Categories
from ProductApp.views import product_detail,order_detail,categorie_detail

urlpatterns = [
    path('products/', products),
    path('products/<int:pk>', product_detail),
    path('orders/', Orders),
    path('orders/<int:pk>', order_detail),
    path('categories/', Categories),
    path('categories/<int:pk>', categorie_detail),
]
