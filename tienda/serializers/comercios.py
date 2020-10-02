"""Comercios serializaers."""

#Django REST Framework
from rest_framework import serializers

class ComercioLoginSerializer(serializers.Serializer):
  """Comercio login serializer"""

  username=serializers.CharField()
  password=serializers.CharField(min_length=8)