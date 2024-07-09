from django.urls import path, re_path, include
#
from . import views

app_name = 'producto_app'


urlpatterns = [
    path('productos/', views.ProdeuctosView.as_view(), name='productos'),
    path('nuevo-producto/', views.RegistrarProductoView.as_view(), name='nuevo_producto'),
]