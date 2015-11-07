# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect, HttpResponse
from django.views.generic import View, ListView, DeleteView
from apps.cliente.models import Cliente
from apps.facturacion.models import Venta
from apps.receta.models import Receta
from .models import Producto,Proveedor
from .forms import ProductoForm,IngresoProductosForm
from django.contrib import messages
from apps.usuarios.views import LoginRequiredMixin
from decimal import Decimal



class Index(LoginRequiredMixin,View):
    template_name = 'index.html'
    def get(self,request):
        import datetime
        datetime.date.today()
        proveedores = Proveedor.objects.all()
        #receta = Receta.objects.all().order_by('-fecha').distinct("cliente")
        receta = Receta.objects.all().order_by('-fecha')
        lista = []
        for item in receta:
            diff = (datetime.date.today() - item.fecha).days
            if(int(diff/30) >= 8):
                lista.append(item)
        receta = lista
        ventas = Venta.objects.all()
        suma_mes = Decimal(0)
        suma_dia = Decimal(0)
        for item in ventas:
            if item.fecha == datetime.date.today():
                suma_dia += Decimal(item.importe)
            if item.fecha.month == datetime.date.today().month:
                suma_mes += Decimal(item.importe)
        clientes = Cliente.objects.filter(fecha_nacimiento__month=datetime.date.today().month, fecha_nacimiento__day=datetime.date.today().day)
        return render(request,self.template_name,locals())

class Productos(LoginRequiredMixin,View):
    template_name = 'productos/index.html'
    def get(self,request):
        productos = Producto.objects.all()
        producto_form = ProductoForm()
        ingreso_form = IngresoProductosForm()
        return render(request,self.template_name,locals())
    def post(self,request):
        productos = Producto.objects.all()
        producto_form = ProductoForm(request.POST)
        ingreso_form = IngresoProductosForm(request.POST)
        if producto_form.is_valid():
            producto = producto_form.save()
            messages.success(request, 'El producto '+str(producto.descripcion)+' de código '+str(producto.codigo)+' fue registrado con exito')
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresoProductosForm()
            return render(request,self.template_name,locals())
        elif(ingreso_form.is_valid()):
            historial = ingreso_form.save()
            producto = Producto.objects.get(pk=historial.producto.id)
            producto.stock_actual += int(request.POST['cantidad'])
            producto.save()
            messages.success(request, 'Se ingresaron '+request.POST['cantidad']+' unidades de '+producto.descripcion)
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresoProductosForm()
            return render(request,self.template_name,locals())
        else:
            messages.error(request, 'No se pudo registrar la operación, porfavor intente denuevo.')
            return render(request,self.template_name,locals())

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ObtenerProducto(request,nro):
    item = Producto.objects.get(pk=nro)
    return HttpResponse(json.dumps({"precio":float(item.precio_sugerido),"max_value":item.stock_actual}),content_type='application/json')

