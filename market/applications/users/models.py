from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):

    ADMINISTRADOR = '0'
    ALMACENISTA = '1'
    VENDEDOR = '2'

    CHOICES_OCUPATION = (
        (ADMINISTRADOR, 'Administrador'),
        (ALMACENISTA, 'Almacenista'),
        (VENDEDOR, 'Vendedor')
    )


    FEMENINO = '0'
    MASCULINO = '1'
    OTRO = '2'

    CHOICES_GENERO = (
        (FEMENINO, 'Femenino'),
        (MASCULINO, 'Masculino'),
        (OTRO, 'otro')
    )


    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=150)
    ocupation = models.CharField('Ocupacion', max_length=1, choices=CHOICES_OCUPATION, blank=True)
    genero = models.CharField('Genero', max_length=1, choices=CHOICES_GENERO, blank=True)
    date_birth = models.DateField('Fecha Nacimiento', blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    
    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]


    def get_full_name(self):
        return self.full_name


    def get_email(self):
        return self.email