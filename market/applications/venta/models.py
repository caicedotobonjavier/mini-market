from django.db import models
#
from model_utils.models import TimeStampedModel
#
from django.conf import settings
#
from applications.producto.models import Product
#
from .managers import CarritoComprasManager, SaleDetailManager
# Create your models here.


class Sale(TimeStampedModel):
    """Modelo que representa una venta"""

    BOLETA = '0'
    FACTURA = '1'
    SIN_COMPROBANTE = '2'

    CHOICES_TYPE_INVOCE = (
        (BOLETA, 'Boleta'),
        (FACTURA, 'Factura'),
        (SIN_COMPROBANTE, 'Sin Comprobante')
    )


    TARJETA = '0'
    EFECTIVO = '1'
    BONOS = '2'
    OTRO = '3'

    CHOICES_TYPE_PAYMENT = (
        (TARJETA, 'Tarjeta'),
        (EFECTIVO, 'Efectivo'),
        (BONOS, 'Bonos'),
        (OTRO, 'Otros')
    )


    date_sale = models.DateField('Fecha de venta')
    count = models.PositiveIntegerField('Cantidad de productos')
    amount = models.PositiveIntegerField('Monto Total')
    type_invoce = models.CharField('Tipo factura', max_length=1, choices=CHOICES_TYPE_INVOCE)
    type_payment = models.CharField('Tipo de pago', max_length=1, choices=CHOICES_TYPE_PAYMENT)
    close = models.BooleanField('Venta cerrada', default=False)
    anulate = models.BooleanField('Venta anulada', default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name= 'cajero', related_name='user_venta', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    

    def __str__(self):
        return 'N°-[' + str(self.id) + '] - ' + str(self.date_sale) + ']'




class SaleDetail(TimeStampedModel):
    """Modelo para los detalles de las ventas"""

    product = models.ForeignKey(Product, related_name='product_sale', verbose_name='producto' ,on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, related_name='detail_sale', verbose_name='Codigo de Venta' ,on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Cantidad')
    price_purchase = models.PositiveIntegerField('Precio de Compra')
    price_sale = models.PositiveIntegerField('Precio de Venta')
    tax = models.PositiveIntegerField('Impuesto', default=19)
    anulate = models.BooleanField(default=False)

    objects = SaleDetailManager()

    class Meta:
        verbose_name = 'Producto Vendido'
        verbose_name_plural = 'Productos Vendidos'
    

    def __str__(self):
        return str(self.id) + ' - ' + str(self.product.name)



class CarShop(TimeStampedModel):
    """Modelo para el carrito de compras"""

    barcode = models.CharField('Codigo barras', max_length=10, unique=True)
    product = models.ForeignKey(Product, related_name='product_car', verbose_name='producto', on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Cantidad')

    objects = CarritoComprasManager()

    class Meta:
        verbose_name = 'Carrito Compra'
        verbose_name_plural = 'Carrito Compras'
        ordering = ['-created']
    

    def __str__(self):
        return str(self.product.name)