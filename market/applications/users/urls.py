from django.urls import path, re_path, include
#
from . import views

app_name = 'usuarios_app'


urlpatterns = [
    path('crear-usuario/', views.CrearUsuarioView.as_view(), name='nuevo_usuario'),
    path('login-usuario/', views.LoginUserView.as_view(), name='login_usuario'),
    path('logout/', views.LoguotView.as_view(), name='logout'),
]
