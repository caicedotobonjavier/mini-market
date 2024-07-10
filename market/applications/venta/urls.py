from django.urls import path, re_path, include
#
from . import views

app_name = 'venta_app'


urlpatterns = [
    path('ventas/', views.VentasView.as_view(), name='venta'),
    path('aumentar-articulo/<pk>/', views.AumentarCantidadArticuloView.as_view(), name='aumentar'),
    path('eliminar-articulo/<pk>/', views.EliminarArticuloCarritoView.as_view(), name='eliminar'),
    path('comprar/', views.RealizarCompraView.as_view(), name='comprar'),
]