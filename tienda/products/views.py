"""Producs views"""

#Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Models
from tienda.products.models import Product

#Serializer
from tienda.products.serelizers import ProductSerializer,CreateProductSerializer

@api_view(['GET'])
def list_products(request):
  """List Products."""
  products = Product.objects.filter(is_public = True)
  serializer = ProductSerializer(products, many=True)
  data=[]
  return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
  """Create product."""
  serializer = CreateProductSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  product=serializer.saver()
  return Response(ProductSerializer(product).data)