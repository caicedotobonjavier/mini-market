import datetime
#
from django.shortcuts import render
#
from .models import Sale, SaleDetail, CarShop
#
from applications.producto.models import Product
#
from django.views.generic import TemplateView, FormView, View, ListView
#
from .forms import CarritoComprasForm
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect, HttpResponse
#
from .functions import crear_venta
#
from .utils import factura_pdf
#
from django.db.models import Sum
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


#para ver esto en pdf se debe instalar xhtml2pdf, este paquete nos sirve para covertir un html en pdf
class ListaCarritoCompras(ListView):
    template_name = 'venta/lista-compras.html'
    model = CarShop
    context_object_name = 'productos'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_pagar"] = CarShop.objects.total_pagar()
        return context



#vista para generar la factura
class FacturaView(View):

    def post(self, request, *args, **kwargs):

        #productos para enviar a el template de factura
        productos = CarShop.objects.all()

        #cantidad de productos para enviar a el template de factura
        cantidad = CarShop.objects.all().aggregate(
            suma = Sum('count')
        )

        #total a pagar
        total_pagar = CarShop.objects.total_pagar()


        print(cantidad)

        data = {
            'productos' : productos,
            'cantidad' : cantidad,
            'total_pagar' : total_pagar,
        }

        pdf = factura_pdf('venta/factura.html', data)

        return HttpResponse(pdf, content_type='application/pdf')