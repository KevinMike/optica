from django import forms
from .models import Cliente
import datetime

class ClienteForm(forms.ModelForm):
    dni = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'DNI','required':'true',}),label="DNI")
    nombre = forms.CharField(max_length=45,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','required':'true',}),label="Nombre")
    apellido = forms.CharField(max_length=45,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido','required':'true',}),label="Apellido")
    direccion = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),label="Telefono")
    email = forms.EmailField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo Electronico'}),label="Email")
    fecha_nacimiento = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'class':'form-control',}),label="Fecha de Nacimiento")
    ocupacion = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ocupacion'}),label="Ocupacion")
    foto = forms.ImageField()

    class Meta:
        model = Cliente
        fields = ('dni','nombre','apellido','direccion','telefono','email','fecha_nacimiento','ocupacion','foto',)