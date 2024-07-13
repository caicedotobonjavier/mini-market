from django.shortcuts import render
#
from django.urls import reverse_lazy
#
from django.contrib.auth import login, logout, authenticate
#
from .models import User
#
from django.views.generic import FormView, View
#
from .forms import RegistrarUsuarioForm, LoginUserForm
#
from django.http import HttpResponseRedirect
#
from django.urls import reverse
# Create your views here.



class CrearUsuarioView(FormView):
    template_name = 'user/registro-usuario.html'
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy('usuarios_app:nuevo_usuario')


    def form_valid(self, form):

        email = form.cleaned_data['email']
        full_name = form.cleaned_data['full_name']
        ocupation = form.cleaned_data['ocupation']
        genero = form.cleaned_data['genero']
        date_birth = form.cleaned_data['date_birth']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        usuario = User.objects.create_user(
            form.cleaned_data['email'],
            full_name = full_name,
            ocupation = ocupation,
            genero = genero,
            date_birth = date_birth,
        )
        usuario.set_password(password1)
        usuario.save()

        return super(CrearUsuarioView, self).form_valid(form)



class LoginUserView(FormView):
    template_name = 'user/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('venta_app:venta')


    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(email=email, password=password)

        login(self.request, user)

        return super(LoginUserView, self).form_valid(form)



class LoguotView(View):

    def post(self, request, *args, **kwargs):
        
        logout(request)
        
        return HttpResponseRedirect(
            reverse(
                'usuarios_app:login_usuario'
            )
        )