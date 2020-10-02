"""Profile model."""

#Django
from django.db import models

#Utilities
from tienda.utils.models import TiendaModel

class Profile(TiendaModel):
      """Profile model.
      A profile holds a comercio's public data like picture, address and staticts.
      """

      comercio = models.OneToOneField('comercios.Tienda',on_delete=models.CASCADE)

      picture = models.ImageField(
        'profile picture',
        upload_to='comercios/pictures/',
        blank=True,
        null=True,
        height_field=None,
        width_field=None,
        max_length=None
        )

      sede_name = models.TextField(max_length=500, blank=True)

      address = models.TextField(max_length=500, blank=True)

      #Stats
      sales_made = models.PositiveIntegerField(default=0)
      stock = models.PositiveIntegerField(default=0)
      reputation = models.FloatField(
        default = 5.0,
        help_text = "Comercio's reputation based on the sales made"
      )

      def __str__(self):
        """Return comercio's str representation"""
        return str(self.user)