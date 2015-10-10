from django import forms
from django.forms.formsets import formset_factory
from .models import Venta,DetalleVenta,Producto
import datetime

class VentaForm(forms.ModelForm):
    def get_nro():
        try:
            ultima_venta = Venta.objects.latest('nro')
            return ultima_venta.nro + 1
        except Venta.DoesNotExist:
            return 1


    nro = forms.IntegerField(initial=get_nro,label="Numero de Venta",widget=forms.NumberInput(attrs={'class':'form-control','min':'0','required':'true'}))
    observaciones = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control',}),)

    class Meta:
        model = Venta
        fields = ('nro','observaciones',)

class DetalleVentaForm(forms.ModelForm):
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-control c-producto','required':'true',}),
                                        label="Producto",empty_label="Seleccione un Producto")
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true', 'placeholder':'Precio','min':'0'}),label="Precio")

    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true','placeholder':'Unidades','min':'0'}),label="Cantidad")

    class Meta:
        model = DetalleVenta
        fields = ('codigo_producto','precio','cantidad')

DetalleVentaFormSet =formset_factory(DetalleVentaForm, extra=1, max_num=10)