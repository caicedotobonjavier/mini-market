from django.shortcuts import render
#
from .models import Sale, SaleDetail, CarShop
#
from applications.producto.models import Product
#
from django.views.generic import TemplateView, FormView
#
from .forms import CarritoComprasForm
#
from django.urls import reverse_lazy
# Create your views here.


class VentasView(FormView):
    template_name = 'venta/ventas.html'
    form_class = CarritoComprasForm
    success_url = reverse_lazy('venta_app:venta')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["carrito"] = CarShop.objects.productos_carrito()        
        return context
    

    def form_valid(self, form):

        barcode = form.cleaned_data['barcode']
        count = form.cleaned_data['count']

        producto, created = CarShop.objects.get_or_create(
            barcode = barcode,
            defaults={
                'product' : Product.objects.get(barcode=barcode),
                'count' : count
            }
        )

        if producto:
            producto.count += count
            producto.save()

        return super(VentasView, self).form_valid(form)