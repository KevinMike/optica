# -*- encoding: utf-8 -*-
from django import forms
from .models import *

class IngresarProductoForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
                                        label="Producto",empty_label="Seleccione un Producto")
    cantidad = forms.IntegerField(initial=0,label="Cantidad",widget=forms.NumberInput(attrs={'class':'form-control','min':'0','required':'true',}))

class ProductoForm(forms.ModelForm):
    codigo = forms.CharField(max_length=5,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Código',}),label="Código",required=False,)
    descripcion = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción','required':'true'}),label="Descripción")
    marca = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Marca',}),label="Marca",required=False,)
    color = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Color',}),label="Color",required=False,)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
                                        label="Categoría",empty_label="Seleccione una Categoria")
    longitud = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Longitud',}),label="Longitud",required=False,)
    precio_sugerido = forms.IntegerField(initial=0,label="Precio Sugerido",widget=forms.NumberInput(attrs={'class':'form-control','min':'0',}))
    stock_minimo = forms.IntegerField(initial=0,label="Stock Mínimo",widget=forms.NumberInput(attrs={'class':'form-control','min':'0',}))
    stock_actual = forms.IntegerField(initial=0,label="Stock Actual",widget=forms.NumberInput(attrs={'class':'form-control','min':'0'}))

    class Meta:
        model = Producto
        fields = ('codigo','descripcion','marca','color','categoria','longitud','precio_sugerido','stock_minimo','stock_actual')

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','required':'true',}),label="Nombre")
    descripcion = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Categoria
        fields = ('nombre','descripcion',)