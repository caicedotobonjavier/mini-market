from django.urls import path, re_path, include
#
from . import views

app_name = 'venta_app'


urlpatterns = [
    path('ventas/', views.VentasView.as_view(), name='venta'),
]