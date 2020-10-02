"""Comercios URLs."""
#Django
from django.urls import path

#Views
from tienda.comercios.views import ComercioLoginAPIView

urlpatterns = [
    path('comercios/login',ComercioLoginAPIView.as_view(),name='login'),
]
