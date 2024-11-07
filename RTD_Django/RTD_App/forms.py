from django import forms
from .models import Pedido
from django.core.exceptions import ValidationError

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'email', 'telefono_cliente', 'comentario']

    def clean_telefono_cliente(self):
        telefono = self.cleaned_data.get('telefono_cliente')
        if len(str(telefono)) != 10:
            raise ValidationError('El número de contacto debe tener 10 dígitos.')
        return telefono

    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario')
        if len(comentario) > 200:
            raise ValidationError('El comentario debe tener menos de 200 caracteres.')
        return comentario
