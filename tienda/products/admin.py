"""Products admin."""

# Django
from django.contrib import admin

#Models
from tienda.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin."""

    list_display =(
      'slug_name',
      'product_name',
      'product_sell',
      'product_stock',
      'product_attribute',
      'is_public'
    )

    search_fields=('slug_name','product_name')

    list_filter = (
      'product_stock',
    )