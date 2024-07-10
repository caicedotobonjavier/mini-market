from django.shortcuts import render
#
from .models import Product
#
from applications.venta.models import SaleDetail
#
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DetailView
#
from .forms import NuevoProductoForm, ActualizarProductoForm
#
from django.urls import reverse, reverse_lazy
# Create your views here.


class ProdeuctosView(TemplateView):
    template_name = 'producto/producto.html'


    def get_context_data(self, **kwargs):
        context = super(ProdeuctosView, self).get_context_data(**kwargs)

        dato = self.request.GET.get('producto')
        ordenar = self.request.GET.get('order')
        context["productos"] = Product.objects.todos_los_productos(dato, ordenar)
        return context



class RegistrarProductoView(FormView):
    template_name = 'producto/registro_productos.html'
    form_class = NuevoProductoForm
    success_url = reverse_lazy('producto_app:productos')


    def form_valid(self, form):

        Product.objects.create(
            barcode = form.cleaned_data['barcode'],
            name = form.cleaned_data['name'],
            provider = form.cleaned_data['provider'],
            marca = form.cleaned_data['marca'],
            due_date = form.cleaned_data['due_date'],
            description = form.cleaned_data['description'],
            unit = form.cleaned_data['unit'],
            count = form.cleaned_data['count'],
            purchase_price = form.cleaned_data['purchase_price'],
            sale_price = form.cleaned_data['sale_price']
        )
        

        return super(RegistrarProductoView, self).form_valid(form)



class ActualizarProductoView(UpdateView):
    template_name = 'producto/update-producto.html'
    form_class = ActualizarProductoForm
    model = Product

    success_url = reverse_lazy('producto_app:productos')



class DetallesDelProductoView(DetailView):
    template_name = 'producto/detalles-producto.html'
    model = Product
    context_object_name = 'producto'


    def get_context_data(self, **kwargs):
        context = super(DetallesDelProductoView, self).get_context_data(**kwargs)

        producto = self.kwargs['pk']
        context["venta_producto"] = SaleDetail.objects.producto_veces_vendido(producto)
        return context
    