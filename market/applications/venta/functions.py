import datetime
#
from .models import CarShop, Sale, SaleDetail
#
from applications.producto.models import Product


def crear_venta(self, **datos_venta):
    """proceso para realizar la venta"""
    
    carrito = CarShop.objects.all()

    #valido que el carrito tenga productos
    if len(carrito) > 0:    
        
        #realizado el registro de la venta
        venta = Sale.objects.create(
            date_sale = datetime.datetime.now(),
            count = 0,
            amount  = 0,
            type_invoce  = datos_venta['type_invoce'],
            type_payment  = datos_venta['type_payment'],
            user  = datos_venta['user'],
        )

        #declaro unas variables locales para acumular cantidad, monto y lista de productos
        count = 0
        amount = 0
        lista_productos = []
        list_stock = []

        #recorro los productos en el carrito y los guardo en la venta detalle
        for producto in carrito:
            add = SaleDetail(
                product = producto.product,
                sale = venta,
                count = producto.count,
                price_purchase = producto.product.purchase_price,
                price_sale = producto.product.sale_price
            )

            #acumulo la cantidad, monto y lista de productos
            count += producto.count
            amount += producto.count * producto.product.sale_price
            lista_productos.append(add)

            #cada vez que recorro el producto lo guardo en variable para actualiar el stock y la cantidad de veces vendido
            producto_vendido = producto.product
            producto_vendido.count -= producto.count
            producto_vendido.num_sale += producto.count
            
            list_stock.append(producto_vendido)
        
        #guardo todos los productos con su respectivo detalle
        SaleDetail.objects.bulk_create(
            lista_productos
        )

        Product.objects.bulk_update(
            list_stock, ['count', 'num_sale']
        )
        
        #acutalizo la cantidad y el monto de la venta
        venta.count = count
        venta.amount = amount
        venta.save()        

        #luegio de la venta elimino todo los productos del carrito
        carrito.delete()

    else:
        print('Carrito vacio')