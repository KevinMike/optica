# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect
from django.views.generic import View, ListView, DeleteView
from apps.cliente.forms import ClienteForm
from .forms import VentaForm,DetalleVentaFormSet,DetalleLenteFormSet,PagarNota
from .models import *
from django.contrib import messages
import datetime
from apps.usuarios.views import LoginRequiredMixin
# Create your views here.
class IndexView(LoginRequiredMixin, View):
    template_name= "facturacion/index.html"
    def get(self,request):
        cliente_form = ClienteForm()
        venta_form = VentaForm()
        DetalleFormSet = DetalleVentaFormSet(prefix='formset_producto')
        LenteFormSet = DetalleLenteFormSet(prefix='formset_lente')
        return render(request,self.template_name,locals())
    def post(self,request):
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
            DetalleFormSet = DetalleVentaFormSet(request.POST,prefix='formset_producto')
            LenteFormSet = DetalleLenteFormSet(request.POST,prefix='formset_lente')
            if DetalleFormSet.is_valid() and LenteFormSet.is_valid():
                if request.POST['BuscarCliente']: #El if verifica si existe un cliente
                    cliente = Cliente.objects.get(pk=request.POST['BuscarCliente'])
                    if cliente:
                        venta.dni_cliente = cliente
                venta.save()
                total = 0 #variable para calcular el subtotal
                for item in DetalleFormSet: #Guardar Detalles Productos
                    detalle = item.save(commit=False)
                    detalle.nro_venta = venta
                    detalle.save()
                    total = total + (detalle.precio)*int(detalle.cantidad)
                for item in LenteFormSet: #Guardar Detalles Lentes
                    detalle = item.save(commit=False)
                    detalle.nro_venta = venta
                    detalle.save()
                    total = total + (detalle.precio)
                    item.save_m2m()
                venta = Venta.objects.get(pk=venta.nro) #Actualizar venta
                print type(request.POST['tipo_recibo'])
                flag = str(request.POST['tipo_recibo'])
                if flag == "True": #Boleta de Venta
                    if ( float(request.POST['importe']) >= float(total) ):
                        print "importe correcto"
                        venta.cancelado = True
                        venta.importe = float(request.POST['importe'])
                        venta.total = total
                        venta.saldo = total-venta.importe
                        venta.save()
                    else: #Importe incorrecto, eliminar datos
                        venta.delete()
                        messages.error(request, 'No se pudo registrar la venta, el importe ingresado no es suficiente.')
                        cliente_form = ClienteForm()
                        return render(request,self.template_name,locals())
                else:   #Nota de Pedido
                    nota = NotaPedido()
                    nota.venta = venta
                    nota.importe = int(request.POST['importe'])
                    nota.saldo = float(total) - float(request.POST['importe'])
                    nota.save()
                    print "Nota de pedido"
                    venta.cancelado = False
                    venta.importe = int(request.POST['importe'])
                    venta.total = total
                    venta.saldo = total-venta.importe
                    venta.save()
                messages.success(request, 'La venta número '+ str(venta.nro) +' se registro con éxito')
                return  redirect('reporte/'+str(venta.nro))
            else:
                messages.error(request, 'No se pudo registrar la venta, ocurrio un error en el formulario detalles de venta.')
                cliente_form = ClienteForm()
                return render(request,self.template_name,locals())
        else:
            messages.error(request, 'No se pudo registrar la venta, ocurrio un error en el formulario de venta.')
            DetalleFormSet = DetalleVentaFormSet(request.POST,prefix='formset')
            cliente_form = ClienteForm()
            return render(request,self.template_name,locals())

class HistorialView(LoginRequiredMixin,View):
    template_name = 'facturacion/historial_ventas.html'
    def get(self,request):
        ventas = Venta.objects.order_by('-total')
        return render(request,self.template_name,locals())

class NotaPedidoView(LoginRequiredMixin,View):
    template_name = 'facturacion/historial_notas_pedido.html'
    def get(self,request):
        notas = NotaPedido.objects.order_by('id')
        return render(request,self.template_name,locals())


class NotaPedidoPayment(View):
    template_name = 'facturacion/nota_pedido.html'
    def get(self,request,nro):
        nota = NotaPedido.objects.get(pk=nro)
        venta = Venta.objects.get(pk=nota.venta.nro)
        detalles = DetalleVenta.objects.filter(nro_venta=nota.venta.nro)
        lentes = DetalleLente.objects.filter(nro_venta=nota.venta.nro)
        form = PagarNota()
        return render(request,self.template_name,locals())
    def post(self,request,nro):
        nota = NotaPedido.objects.get(pk=nro)
        nota.importe = nota.importe + nota.saldo
        nota.saldo = 0
        nota.save()
        venta = Venta.objects.get(pk=nota.venta.nro)
        venta.importe = venta.total
        venta.saldo = 0
        venta.cancelado = True
        venta.save()
        return redirect('/')

def reporte(request,nro):
    template_name = 'facturacion/reporte.html'
    venta = Venta.objects.get(pk=nro)
    detalles = DetalleVenta.objects.filter(nro_venta=nro)
    lentes = DetalleLente.objects.filter(nro_venta=nro)
    return render(request,template_name,locals())


def estadisticas(request):
    venta = Venta.objects.all()
    pass
