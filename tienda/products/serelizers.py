"""Product sereliezers."""

# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from tienda.products.models import Product

class ProductSerializer (serializers.Serializer):
  """Product sereliezers."""
  product_name =serializers.CharField()
  slug_name=serializers.SlugField()
  description =serializers.CharField()
  product_sell=serializers.IntegerField()
  product_stock=serializers.IntegerField()
  product_attribute =serializers.CharField()

class CreateProductSerializer(serializers.Serializer):
  """Create Product sereliezers."""
  product_name =serializers.CharField(max_length=140)
  slug_name=serializers.SlugField(max_length=40, validators=[
    UniqueValidator(queryset=Product.objects.all())
  ])
  description =serializers.CharField(max_length=255, required=False)
  product_sell=serializers.IntegerField()
  product_stock=serializers.IntegerField()
  product_attribute =serializers.CharField()

  def create(self, data):
    """Create Product"""
    return Product.objetcs.create(**data)
