from django.contrib import admin
#
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'full_name',
        'ocupation',
        'genero',
        'date_birth',
        'is_staff',
        'is_active',
        'is_superuser',
    )


admin.site.register(User, UserAdmin)