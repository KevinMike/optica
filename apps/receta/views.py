# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from .forms import RecetaForm
from apps.cliente.forms import ClienteForm
from apps.cliente.models import Cliente
from django.contrib import messages
import datetime
# Create your views here.
class Index(View):
    template_name = 'receta/index.html'
    def get(self,request):
        form = RecetaForm()
        cliente_form = ClienteForm
        return render(self.request,self.template_name,locals())
    def post(self,request):

        try:
            cliente = Cliente.objects.get(dni=request.POST['dni_cliente'])
            form = RecetaForm(request.POST,request.FILES)
            if form.is_valid():
                form.dni_cliente = cliente
                receta = form.save(commit=False)
                receta.fecha = datetime.date.today()
                receta.save()
                form = RecetaForm()
                cliente_form = ClienteForm()
                messages.success(request, 'La medición se registro con éxito.')
                return render(self.request,self.template_name,locals())
            else:
                print form.errors
                cliente_form = ClienteForm
                messages.error(request, 'No se pudo registrar, se produjeron algunos errores.')
                return render(self.request,self.template_name,locals())
        except Cliente.DoesNotExist:
            messages.error(request, 'No se pudo registrar, el cliente seleccionado no existe.')
            form = RecetaForm()
            cliente_form = ClienteForm
            return render(self.request,self.template_name,locals())
