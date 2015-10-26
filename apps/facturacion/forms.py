from django import forms
from django.forms.formsets import formset_factory
from apps.almacen.models import Categoria
from .models import Venta,DetalleVenta,Producto,DetalleLente,Aditivos,Lente
from django.core.exceptions import ValidationError

class VentaForm(forms.ModelForm):
    tipo_pagos = (
        ('True','Boleta de Venta'),
        ('False','Nota de Pedido'),
    )

    def get_nro():
        try:
            ultima_venta = Venta.objects.latest('nro')
            return ultima_venta.nro + 1
        except Venta.DoesNotExist:
            return 1

    nro = forms.IntegerField(initial=get_nro,label="Numero de Venta",widget=forms.NumberInput(attrs={'id':'NroFacturacion','class':'form-control','min':'0','required':'true'}))
    importe = forms.IntegerField(label="Importe del Cliente",widget=forms.NumberInput(attrs={'class':'form-control','min':'0','required':'true'}),)
    observaciones = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','rows':'2'}),required=False,)
    tipo_recibo = forms.ChoiceField(label="Tipo de Pago",widget=forms.Select(attrs={'class':'form-control','required':'true',}),choices=tipo_pagos)
    class Meta:
        model = Venta
        fields = ('nro','observaciones',)

def producto_as_choices():
    categories = []
    for category in Categoria.objects.all():
        new_category = []
        sub_categories = []
        for sub_category in category.producto_set.all():
            sub_categories.append([sub_category.id, sub_category.descripcion])

        new_category = [category.nombre, sub_categories]
        categories.append(new_category)
    return categories

producto_widget = forms.Select(attrs={'class':'prueba form-control chosen-select c-producto ','required':'true',})

class DetalleVentaForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(DetalleVentaForm, self).__init__(*args,**kwargs)
        self.fields['producto'].choices = producto_as_choices
        self.fields['producto'].widget.attrs['class'] = 'form-control c-producto chosen-select'
        # producto = forms.ModelChoiceField(
        #                                    widget=forms.Select(attrs={'class':'prueba form-control chosen-select c-producto ','required':'true',}),
        #                                   label="Producto",empty_label="Seleccione un Producto")
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control ','required':'true', 'placeholder':'Precio','min':'0'}),label="Precio")

    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true','placeholder':'Unidades','min':'0'}),label="Cantidad")
    class Meta:
        model = DetalleVenta
        fields = ('producto','precio','cantidad',)


DetalleVentaFormSet =formset_factory(DetalleVentaForm, extra=1,can_delete=True)

class DetalleLenteForm(forms.ModelForm):
    lente = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
                                        label="Lente",queryset=Lente.objects.all(),empty_label="Seleccione el tipo de Lente",)
    complementos = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'chosen-select chosen-container-multi','required':'true'}),queryset=Aditivos.objects.all(),)
    precio = forms.IntegerField(initial=0,widget=forms.NumberInput(attrs={'class':'form-control','required':'true', 'placeholder':'Precio','min':'0'}),label="Precio",)
    class Meta:
        model = DetalleLente
        fields = ('lente','complementos','precio',)

DetalleLenteFormSet =formset_factory(DetalleLenteForm, extra=1,can_delete=True)

class PagarNota(forms.Form):
    pago = forms.BooleanField(initial=False,widget=forms.CheckboxInput(attrs={'class':'form-control','required':'true',}),label="El cliente ha cancelado su deuda pendiente...")