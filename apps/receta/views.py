# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import RecetaForm
from .models import Receta
from apps.cliente.forms import ClienteForm
from apps.cliente.models import Cliente
from django.contrib import messages
import datetime
from apps.usuarios.views import LoginRequiredMixin
# Create your views here.
class Index(LoginRequiredMixin, View):
    template_name = 'receta/index.html'
    def get(self,request):
        form = RecetaForm()
        cliente_form = ClienteForm
        return render(self.request,self.template_name,locals())
    def post(self,request):
        try:
            cliente_instance = Cliente.objects.get(dni=request.POST['BuscarCliente'])
            form = RecetaForm(request.POST,request.FILES)
            if form.is_valid():
                receta = form.save(commit=False)
                receta.cliente = cliente_instance
                receta.save()
                form.save_m2m()
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

class EditarView(View):
    template_name = 'receta/editar.html'
    def get(self,request,nro):
        receta = Receta.objects.get(pk=nro)
        form = RecetaForm(instance=receta)
        historial = Receta.objects.filter(cliente=receta.cliente).exclude(pk=nro).order_by("-id")
        return render(request,self.template_name,locals())
    def post(self,request,nro):
        receta = Receta.objects.get(pk=nro)
        form = RecetaForm(request.POST,instance=receta)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return redirect("/cliente/")
        else:
            messages.error(request,"No se pudo registrar la medición, existen errores en el formulario.")
            return render(request,self.template_name,locals())