from django import forms
#
from .models import Product


class NuevoProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'barcode',
            'name',
            'provider',
            'marca',
            'due_date',
            'description',
            'unit',
            'count',
            'purchase_price',
            'sale_price',     
        )

        widgets = {
            'barcode' : forms.TextInput(
                attrs={
                    'placeholder' : 'Codigo de barras',
                    'class': 'input-group-field'
                }
            ),

            'name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre producto',
                    'class': 'input-group-field'
                }
            ),

            'purchase_price' : forms.NumberInput(
                attrs= {
                    'placeholder' : 'Precio de compra',
                    'class': 'input-group-field'
                }
            ),

            'sale_price' : forms.NumberInput(
                attrs= {
                    'placeholder' : 'Precio de venta',
                    'class': 'input-group-field'
                }
            ),

            'count' : forms.NumberInput(
                attrs= {
                    'placeholder' : 'Cantidad en almacen',
                    'class': 'input-group-field'
                }
            ),

            'provider' : forms.Select(
                attrs= {
                    'class': 'input-group-field'
                }
            ),

            'unit' : forms.Select(
                attrs= {
                    'class': 'input-group-field'
                }
            ),

            'marca' : forms.Select(
                attrs= {
                    'class': 'input-group-field'
                }
            ),

            'due_date' : forms.DateInput(
                attrs= {
                    'type' : 'date',
                    'class': 'input-group-field'
                }
            ),

            'description' : forms.Textarea(
                attrs= {
                    'placeholder': 'Descripcion del producto',
                    'rows': '3',
                    'class': 'input-group-field'
                }
            ),
        }


    def clean_barcode(self):
        barcode = self.cleaned_data['barcode']
        if len(barcode) < 10:
            raise forms.ValidationError('El codigo debe tener 10 digitos')
        
        return barcode
