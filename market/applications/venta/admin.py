from django.contrib import admin
#
from .models import Sale, SaleDetail, CarShop
# Register your models here.


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date_sale',
        'count',
        'amount',
        'type_invoce',
        'type_payment',
        'close',
        'anulate',
        'user',
    )

admin.site.register(Sale, SaleAdmin)



class SaleDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'sale',
        'count',
        'price_purchase',
        'price_sale',
        'tax',
        'anulate',
    )

admin.site.register(SaleDetail, SaleDetailAdmin)



class CarShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'barcode',
        'product',
        'count',
    )


admin.site.register(CarShop, CarShopAdmin)