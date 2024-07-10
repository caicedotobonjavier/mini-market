import datetime
#
from .models import CarShop, Sale, SaleDetail
#
from applications.producto.models import Product


def crear_venta(self, **datos_venta):

    carrito = CarShop.objects.all()

    if len(carrito) > 0:    
        
        venta = Sale.objects.create(
            date_sale = datetime.datetime.now(),
            count = 0,
            amount  = 0,
            type_invoce  = datos_venta['type_invoce'],
            type_payment  = datos_venta['type_payment'],
            user  = datos_venta['user'],
        )

        count = 0
        amount = 0
        lista_productos = []

        for producto in carrito:
            add = SaleDetail(
                product = producto.product,
                sale = venta,
                count = producto.count,
                price_purchase = producto.product.purchase_price,
                price_sale = producto.product.sale_price
            )

            count += producto.count
            amount += producto.count * producto.product.sale_price
            lista_productos.append(add)
        
        SaleDetail.objects.bulk_create(
            lista_productos
        )
        
        venta.count = count
        venta.amount = amount
        venta.save()

        carrito.delete()

    else:
        print('Carrito vacio') 