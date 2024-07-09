from django.contrib import admin
#
from .models import Product, Marca, Provider
# Register your models here.


class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Marca, MarcaAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'web',
    )


admin.site.register(Provider, ProviderAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'barcode',
        'name',
        'provider',
        'marca',
        'due_date',
        'description',
        'unit',
        'count',
        'purchase_price',
        'sale_price',
        'num_sale',
        'anulate',
    )


admin.site.register(Product, ProductAdmin)