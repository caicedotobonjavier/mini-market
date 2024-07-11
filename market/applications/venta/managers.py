from django.db import models
#
from django.db.models import F, Sum, IntegerField


class CarritoComprasManager(models.Manager):

    def productos_carrito(self):
        return self.all().order_by('barcode')


    def total_pagar(self):
        total = self.aggregate(
            suma = Sum(
                F('product__sale_price') * F('count'),
                output_field = IntegerField()
            )
        )

        if total['suma']:
            return total['suma']
        else:
            return 0




class SaleDetailManager(models.Manager):

    def producto_veces_vendido(self, dato):
        resultado = self.filter(
            product__id = dato
        )

        print(resultado)

        return resultado