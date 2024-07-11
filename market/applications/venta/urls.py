from django.urls import path, re_path, include
#
from . import views

app_name = 'venta_app'


urlpatterns = [
    path('ventas/', views.VentasView.as_view(), name='venta'),
    path('aumentar-articulo/<pk>/', views.AumentarCantidadArticuloView.as_view(), name='aumentar'),
    path('eliminar-articulo/<pk>/', views.EliminarArticuloCarritoView.as_view(), name='eliminar'),
    path('comprar/', views.RealizarCompraView.as_view(), name='comprar'),
    path('productos-car/', views.ListaCarritoCompras.as_view(), name='lista_productos'),
    path('factura/', views.FacturaView.as_view(), name='factura'),
    path('vaciar-carrito/', views.EliminarProductosCarritoView.as_view(), name='vaciar_carrito'),
]