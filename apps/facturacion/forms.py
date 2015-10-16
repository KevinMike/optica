from django import forms
from django.forms.formsets import formset_factory
from .models import Venta,DetalleVenta,Producto,DetalleLente,Aditivos,Lente
import datetime

class VentaForm(forms.Form):
    def get_nro():
        try:
            ultima_venta = Venta.objects.latest('nro')
            return ultima_venta.nro + 1
        except Venta.DoesNotExist:
            return 1
    nro = forms.IntegerField(initial=get_nro,label="Numero de Venta",widget=forms.NumberInput(attrs={'id':'NroFacturacion','class':'form-control','min':'0','required':'true'}))
    importe = forms.IntegerField(initial=0,label="Importe del Cliente",widget=forms.NumberInput(attrs={'class':'form-control','min':'0','required':'true'}))
    observaciones = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','rows':'4'}),)
    class Meta:
        model = Venta
        fields = ('nro','importe','observaciones',)

class DetalleVentaForm(forms.Form):
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-control c-producto chosen-select','required':'true',}),
                                        label="Producto",empty_label="Seleccione un Producto")
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true', 'placeholder':'Precio','min':'0'}),label="Precio")

    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true','placeholder':'Unidades','min':'0'}),label="Cantidad")
    class Meta:
        model = DetalleVenta
        fields = ('codigo_producto','precio','cantidad',)


DetalleVentaFormSet =formset_factory(DetalleVentaForm, extra=10,can_delete=True, max_num=10,)

class DetalleLenteForm(forms.Form):
    lente = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control c-producto chosen-select','required':'true',}),
                                        label="Lente",queryset=Lente.objects.all())

    complementos = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'chosen-select chosen-container-multi','required':'true'}),queryset=Aditivos.objects.all())


    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true', 'placeholder':'Precio','min':'0'}),label="Precio")
    class Meta:
        model = DetalleLente
        fields = ('lente','complementos','precio',)
