from django.db import models


class CarritoComprasManager(models.Manager):

    def productos_carrito(self):
        return self.all()