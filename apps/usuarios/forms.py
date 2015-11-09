# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    #username = forms.CharField(widget= forms.TextInput(attrs={"class":"text", "value":"Usuario", "onfocus":"this.value = '';" ,"onblur":"if (this.value == '') {this.value = 'Usuario';}"}),label="Usuario")
    #password = forms.CharField(widget= forms.PasswordInput(attrs={ "value":"Password", "onfocus":"this.value = '';" ,"onblur":"if (this.value == '') {this.value = 'Password';}" }),label= "Contraseña")
    username = forms.CharField(widget= forms.TextInput(attrs={"class":"text", "placeholder":"Usuario", }),label="Usuario")
    password = forms.CharField(widget= forms.PasswordInput(attrs={ "placeholder":"Password", }),label= "Contraseña")
    #username = forms.CharField(widget= forms.TextInput(attrs={ }),label="Usuario")
    #password = forms.CharField(widget= forms.PasswordInput(attrs={  }),label= "Contraseña")
    class Meta:
        model = User
        fields = ['username', 'password']


