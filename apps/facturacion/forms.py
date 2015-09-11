from django import forms
from django.forms.formsets import formset_factory
from .models import Venta,DetalleVenta,Producto
import datetime

class VentaForm(forms.ModelForm):
    nro = forms.IntegerField(label="Numero de Venta",widget=forms.NumberInput(attrs={'class':'form-control','min':'0'}))
    observaciones = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Venta
        fields = ('nro','observaciones',)

class DetalleVentaForm(forms.ModelForm):
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
                                        label="Producto",empty_label="Seleccione un Producto")
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true', 'placeholder':'Precio','min':'0'}),label="Precio")

    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true','placeholder':'Unidades','min':'0'}),label="Cantidad")

    class Meta:
        model = DetalleVenta
        fields = ('codigo_producto','precio','cantidad')

DetalleVentaFormSet =formset_factory(DetalleVentaForm, extra=1, max_num=10)