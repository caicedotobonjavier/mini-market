from django.db import models
#
from model_utils.models import TimeStampedModel
#
from .managers import ProductoManager
# Create your models here.

class Marca(TimeStampedModel):
    """Marca de los productos"""

    name = models.CharField('Nombre Producto', max_length=30)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    

    def __str__(self):
        return self.name



class Provider(TimeStampedModel):
    """Proveedores de los productos"""

    name = models.CharField('Razon Social', max_length=100)
    email = models.EmailField('Correo Electornico', max_length=254, blank=True, null=True)
    phone = models.CharField('Telefono Contacto', max_length=50, blank=True)
    web = models.URLField('Sitio Web', max_length=200, blank=True)


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proovedores'
    

    def __str__(self):
        return self.name



class Product(TimeStampedModel):
    """Modelo para los Productos"""

    KILOGRAMO = '0'
    LIBRA = '1'
    LITROS = '2'
    UNIDADES = '3'

    UNIT_CHOICES = (
        (KILOGRAMO, 'Kilogramo'),
        (LIBRA, 'Libra'),
        (LITROS, 'Litros'),
        (UNIDADES, 'Unidades')
    )

    barcode = models.CharField('Codigo barras', max_length=10, unique=True)
    name = models.CharField('Nombre producto', max_length=50)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    due_date = models.DateField('Fecha vencimiento', blank=True, null=True)
    description = models.TextField('Descripcion del producto', blank=True)
    unit = models.CharField('Unidad de medida', max_length=1, choices=UNIT_CHOICES)
    count = models.PositiveIntegerField('Cantidad en almacen', default=0)
    purchase_price = models.PositiveIntegerField('Precio compra', default=1)
    sale_price = models.PositiveIntegerField('Precio venta', default=2)
    num_sale = models.PositiveIntegerField('Numero de ventas', default=0)
    anulate = models.BooleanField('Anulado', default=False)

    objects = ProductoManager()


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
    

    def __str__(self):
        return self.name
