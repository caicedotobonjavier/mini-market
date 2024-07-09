from django import forms
#
from .models import CarShop


class CarritoComprasForm(forms.Form):

    barcode = forms.CharField(
        required=True,
        label='Producto',
        widget= forms.TextInput(
            attrs={
                'placeholder' : 'Codigo de barras',
                'class': 'input-group-field',
            }
        )
    )

    count = forms.IntegerField(
        required=True,
        label='Cantidad',
        widget= forms.NumberInput(
            attrs={
                'placeholder' : 'Cantidad',
                'value' : '1',
                'class': 'input-group-field',
            }
        )
    )