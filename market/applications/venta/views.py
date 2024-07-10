import datetime
#
from django.shortcuts import render
#
from .models import Sale, SaleDetail, CarShop
#
from applications.producto.models import Product
#
from django.views.generic import TemplateView, FormView, View
#
from .forms import CarritoComprasForm
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
#
from .functions import crear_venta
# Create your views here.


class VentasView(FormView):
    template_name = 'venta/ventas.html'
    form_class = CarritoComprasForm
    success_url = reverse_lazy('venta_app:venta')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["carrito"] = CarShop.objects.productos_carrito()
        context['total_pagar'] = CarShop.objects.total_pagar()
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

        if not created:
            producto.count += count
            producto.save()

        return super(VentasView, self).form_valid(form)



class AumentarCantidadArticuloView(View):
    
    def post(self, request, *args, **kwargs):
        dato = self.kwargs['pk']
        articulo = CarShop.objects.get(id=dato)
        articulo.count += 1
        articulo.save()

        return HttpResponseRedirect(
            reverse(
                'venta_app:venta'
            )
        )


class EliminarArticuloCarritoView(View):
    
    def post(self, request, *args, **kwargs):
        dato = self.kwargs['pk']
        articulo = CarShop.objects.get(id=dato)
        articulo.delete()

        return HttpResponseRedirect(
            reverse(
                'venta_app:venta'
            )
        )



class RealizarCompraView(View):

    def post(self, request, *args, **kwargs):

        crear_venta(
            self = self,
            type_invoce = Sale.FACTURA,
            type_payment = Sale.EFECTIVO,
            user = self.request.user,
        )


        return HttpResponseRedirect(
            reverse(
                'venta_app:venta'
            )
        )