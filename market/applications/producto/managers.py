from django.db import models
#
from django.db.models import Q


class ProductoManager(models.Manager):

    def todos_los_productos(self, dato, ordenar):
        if dato:
            resultado = self.filter(
                Q(name__icontains = dato) | Q(barcode__icontains = dato)
            )
            return resultado
        
        if ordenar == 'name':
            return self.all().order_by('name')
        elif ordenar == 'date':
            return self.all().order_by('-created')
        elif ordenar == 'stock':
            return self.all().order_by('count')
        else:
            return self.all().order_by('created')