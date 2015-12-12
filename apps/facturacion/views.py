# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View, ListView, DeleteView
from apps.cliente.forms import ClienteForm
from .forms import VentaForm,DetalleVentaFormSet,DetalleLenteFormSet,PagarNota,BloqueVentaForm,BloquePedidoForm
from .models import *
from django.contrib import messages
from apps.usuarios.views import LoginRequiredMixin
from decimal import Decimal
# Create your views here.
def BloqueVenta_last_id():
    try:
        nro = BloqueVenta.objects.get(current=True)
        return nro
    except BloqueVenta.DoesNotExist:
        nro = BloqueVenta.objects.create()
        nro.save()
        return nro

def BloquePedido_last_id():
    try:
        nro = BloquePedido.objects.get(current=True)
        return nro
    except BloquePedido.DoesNotExist:
        nro = BloquePedido.objects.create()
        nro.save()
        return nro

import json
from django.views.decorators.csrf import csrf_exempt

#Obtiene el ultimo numero de pedido
def get_nota_pedido():
    bloque = BloquePedido_last_id()
    print bloque.current
    try:
        ultima_venta = NotaPedido.objects.filter(bloque=bloque.id).order_by('-nro')[0]
        nro = ultima_venta.nro + 1
        return nro
        #return HttpResponse(json.dumps({"nro":nro}),content_type='application/json')
    #except NotaPedido.DoesNotExist:
    except IndexError:
        return 1
        #return HttpResponse(json.dumps({"nro":1}),content_type='application/json')

#Obtiene el ultimo numero de venta
def get_venta():
    bloque = BloqueVenta_last_id()
    print bloque.current
    try:
        ultima_venta = Venta.objects.filter(bloque=bloque.id).order_by('-nro')[0]
        nro = ultima_venta.nro + 1
        return nro
        #return HttpResponse(json.dumps({"nro":nro}),content_type='application/json')
    except IndexError:
        return 1
        #return HttpResponse(json.dumps({"nro":1}),content_type='application/json')




class IndexView(LoginRequiredMixin, View):
    template_name= "facturacion/index.html"
    def get(self,request):
        cliente_form = ClienteForm()
        venta_form = VentaForm()
        DetalleFormSet = DetalleVentaFormSet(prefix='formset_producto')
        LenteFormSet = DetalleLenteFormSet(prefix='formset_lente')
        nro_venta = get_venta()
        nro_pedido = get_nota_pedido()

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
                total = Decimal(0) #variable para calcular el total
                for item in DetalleFormSet: #Guardar Detalles Productos
                    detalle = item.save(commit=False)
                    producto = Producto.objects.get(pk=detalle.producto.id)
                    producto.stock_actual = producto.stock_actual - int(detalle.cantidad)
                    producto.save()
                    detalle.nro_venta = venta
                    detalle.save()
                    total = total + Decimal(detalle.precio)*Decimal(detalle.cantidad)
                for item in LenteFormSet: #Guardar Detalles Lentes
                    detalle = item.save(commit=False)
                    if(detalle.lente != "Ninguno"):
                        detalle.nro_venta = venta
                        detalle.save()
                        total = total + Decimal(detalle.precio)
                        item.save_m2m()
                venta = Venta.objects.get(pk=venta.id) #Actualizar venta
                venta.nro = get_venta()
                venta.bloque = BloqueVenta_last_id()
                flag = str(request.POST['tipo_recibo'])
                if flag == "True": #Boleta de Venta
                    if ( Decimal(request.POST['importe']) >= total ):#importe correcto
                        venta.cancelado = True
                        venta.importe = Decimal(request.POST['importe'])
                        venta.total = Decimal(total)
                        venta.saldo = total-venta.importe
                        venta.save()
                    else: #Importe incorrecto, eliminar datos
                        venta.delete()
                        messages.error(request, 'No se pudo registrar la venta, el importe ingresado no es suficiente.')
                        cliente_form = ClienteForm()
                        return render(request,self.template_name,locals())
                else:   #Nota de Pedido
                    nota = NotaPedido()
                    nota.nro = get_nota_pedido()
                    nota.bloque = BloquePedido_last_id()
                    nota.venta = venta
                    nota.importe = Decimal(request.POST['importe'])
                    nota.saldo = total - Decimal(request.POST['importe'])
                    nota.save()
                    venta.cancelado = False
                    venta.importe = Decimal(request.POST['importe'])
                    venta.total = total
                    venta.saldo = total - venta.importe
                    venta.save()
                messages.success(request, 'La venta número '+ str(venta.nro) +' se registro con éxito')
                return  redirect('reporte/'+str(venta.id))
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
        bloque_form = BloqueVentaForm()
        ventas = Venta.objects.all()
        bloque = BloqueVenta_last_id
        return render(request,self.template_name,locals())

class NotaPedidoView(LoginRequiredMixin,View):
    template_name = 'facturacion/historial_notas_pedido.html'
    def get(self,request):
        notas = NotaPedido.objects.order_by('id')
        bloque_form = BloquePedidoForm()
        bloque = BloquePedido_last_id()
        return render(request,self.template_name,locals())


class NotaPedidoPayment(View):
    template_name = 'facturacion/nota_pedido.html'
    def get(self,request,id):
        nota = NotaPedido.objects.get(pk=id)
        venta = Venta.objects.get(pk=nota.venta.id)
        detalles = DetalleVenta.objects.filter(nro_venta=nota.venta.id)
        lentes = DetalleLente.objects.filter(nro_venta=nota.venta.id)
        form = PagarNota()
        return render(request,self.template_name,locals())
    def post(self,request,id):
        nota = NotaPedido.objects.get(pk=id)
        nota.importe = nota.importe + nota.saldo
        nota.saldo = 0
        nota.save()
        venta = Venta.objects.get(pk=nota.venta.id)
        venta.importe = venta.total
        venta.saldo = 0
        venta.cancelado = True
        venta.save()
        return redirect('/facturacion/notas')
def reporte(request,id):
    template_name = 'facturacion/reporte.html'
    venta = Venta.objects.get(pk=id)
    detalles = DetalleVenta.objects.filter(nro_venta=id)
    lentes = DetalleLente.objects.filter(nro_venta=id)
    return render(request,template_name,locals())

def new_BloqueVenta(request):
    g = BloqueVenta.objects.get(current=True)
    g.current = False
    g.save()
    g = BloqueVenta.objects.create()
    g.save()
    return redirect('/facturacion/historial')

def change_BloqueVenta(request):
    g = BloqueVenta.objects.get(current=True)
    g.current = False
    g.save()
    g = BloqueVenta.objects.get(pk=request.POST['bloque'])
    g.current = True
    g.save()
    return redirect('/facturacion/historial')

def new_BloquePedido(request):
    g = BloquePedido.objects.get(current=True)
    g.current = False
    g.save()
    g = BloquePedido.objects.create()
    g.save()
    return redirect('/facturacion/notas')

def change_BloquePedido(request):
    g = BloquePedido.objects.get(current=True)
    g.current = False
    g.save()
    g = BloquePedido.objects.get(pk=request.POST['bloque'])
    g.current = True
    g.save()
    return redirect('/facturacion/notas')