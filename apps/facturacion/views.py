from django.shortcuts import render,redirect
from django.views.generic import View, ListView, DeleteView
from apps.cliente.forms import ClienteForm
from .forms import VentaForm,DetalleVentaForm,DetalleVentaFormSet
from .models import *
from django.contrib import messages
import datetime
# Create your views here.
class IndexView(View):
    template_name= "facturacion/index.html"
    def get(self,request):
        cliente_form = ClienteForm()
        venta_form = VentaForm()
        DetalleFormSet = DetalleVentaFormSet(prefix='formset')
        return render(request,self.template_name,locals())
    def post(self,request):
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
            venta.fecha = datetime.date.today()
            DetalleFormset = DetalleVentaFormSet(request.POST,prefix='formset')
            if DetalleFormset.is_valid():
                #Verificar Cliente
                if request.POST['BuscarCliente']:
                    cliente = Cliente.objects.get(pk=request.POST['BuscarCliente'])
                    if cliente:
                        venta.dni_cliente = cliente
                venta.save()
                subtotal = 0
                for item in DetalleFormset:
                    detalle = item.save(commit=False)
                    detalle.nro_venta = venta
                    detalle.save()
                    subtotal = subtotal + (detalle.precio) * int(detalle.cantidad)
                venta = Venta.objects.get(pk=venta.nro)
                venta.subtotal = subtotal
                venta.save()
                messages.success(request, 'La venta se registro con exito')
                cliente_form = ClienteForm()
                venta_form = VentaForm()
                DetalleFormSet = DetalleVentaFormSet(prefix='formset')
                return render(request,self.template_name,locals())
            else:
                messages.error(request, 'No se pudo registrar la venta, ocurrio un error en el formulario detalles de venta.')
                cliente_form = ClienteForm()
                return render(request,self.template_name,locals())
        else:
            print venta_form.errors
            messages.error(request, 'No se pudo registrar la venta, ocurrio un error en el formulario de venta.')
            DetalleFormSet = DetalleVentaFormSet(request.POST,prefix='formset')
            cliente_form = ClienteForm()
            return render(request,self.template_name,locals())