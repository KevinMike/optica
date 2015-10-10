from django import forms
from .models import Receta
from apps.cliente.models import Cliente
class RecetaForm(forms.ModelForm):
    dni_cliente = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'DNI','required':'true','onkeyup':'search_client()',}),label="DNI")
    #dni_cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(),
     #                                   widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
      #                                  label="Cliente",empty_label="Pasciente")
    imagen = forms.ImageField()
    class Meta:
        model = Receta
        fields = ('dni_cliente','imagen',)