"""Products URLs."""
#Django
from django.urls import path

#Views
from tienda.products.views import list_products, create_product

urlpatterns = [
    path('products/',list_products),
    path('products/create',create_product)
]
