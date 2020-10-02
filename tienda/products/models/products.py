"""Product model."""

#Django
from  django.db import models

#Utilities
from tienda.utils.models import TiendaModel

class Product(TiendaModel):
  """ Product model.

  A producto is a stock that the user can buy
  """

  product_name = models.CharField('product name', max_length=140)
  slug_name = models.SlugField(unique=True, max_length=40)

  description = models.CharField('product description', max_length=255)
  picture = models.ImageField(upload_to='products/pictures', blank=True, null=True)

  #Stats
  product_sell = models.PositiveIntegerField(default=0)
  product_stock = models.PositiveIntegerField(default=0)
  product_attribute=models.CharField('product atttibute', max_length=210)

  is_public=models.BooleanField(
    default=True,
    help_text='If this product should sell'
  )

  def __str__(self):
      return self.name

  class Meta(TiendaModel.Meta):
    """Meta Class"""
    ordering = ['-product_sell','-product_stock']