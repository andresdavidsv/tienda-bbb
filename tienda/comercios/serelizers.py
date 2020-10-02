"""Comercio sereliezers."""

# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from tienda.comercios.models import comercios

class ComercioLoginSerializaer (serializers.Serializer):
  """Comercio sereliezers."""
  sede_name =serializers.CharField()
  address=serializers.CharField()
