from django.shortcuts import render
#
from .models import Product
#
from django.views.generic import TemplateView, CreateView, FormView
#
from .forms import NuevoProductoForm
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
