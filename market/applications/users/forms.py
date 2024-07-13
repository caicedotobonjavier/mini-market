from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate


class RegistrarUsuarioForm(forms.ModelForm):

    password1 = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Ingrese contraseña'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirme contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )

        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo electronico'
                }
            ),

            'full_name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre completo'
                }
            ),

            'date_birth' : forms.TextInput(
                attrs={
                    'type' : 'date'
                }
            ),
        }


    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        password1 = self.cleaned_data['password1']

        if password2 != password1:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password2


class LoginUserForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label='Correo electronico',
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Correo del usuario'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña del usuario'
            }
        )
    )


    def clean(self):
        cleaned_data = super(LoginUserForm, self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Usuario o contraseña erroneo')

        return self.cleaned_data
