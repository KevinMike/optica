from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['stock_actual']


class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','required':'true',}),label="Nombre")
    descripcion = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Categoria
        fields = ('nombre','descripcion',)