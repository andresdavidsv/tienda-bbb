"""Comercios views."""

#Django REST Framework
from rest_framework import status
from rest_framework.views import APIView

#Serializers
from tienda.comercios.serelizers import ComercioLoginSerializaer

class ComercioLoginAPIView(APIView):
  """Comercio login API view."""
  def post(self, request,*args,**kwargs):
    """Handle HTTP POST requests."""
    serializer = ComercioLoginSerializaer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.save()
    data ={
      'status':'ok',
      'token':token
    }
    return Response(data,status=status.HTTP_201_CREATED)