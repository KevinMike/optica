# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect, HttpResponse
from django.views.generic import View, ListView, DeleteView
from apps.cliente.models import Cliente
from apps.facturacion.models import Venta
from .models import Producto
from .forms import ProductoForm,IngresarProductoForm
from django.contrib import messages
from apps.usuarios.views import LoginRequiredMixin
import datetime

class Index(LoginRequiredMixin,View):
    template_name = 'index.html'
    def get(self,request):
        ventas = Venta.objects.all()
        suma_mes = 0
        suma_dia = 0
        for item in ventas:
            if item.fecha == datetime.date.today():
                suma_dia = suma_dia + item.total
            if item.fecha.month == datetime.datetime.now().month:
                suma_mes = suma_mes + item.total
        clientes = Cliente.objects.all()
        return render(request,self.template_name,{'clientes':clientes,'suma_mes':suma_mes,'suma_dia':suma_dia,})

class Productos(View):
    template_name = 'productos/index.html'
    def get(self,request):
        productos = Producto.objects.all()
        producto_form = ProductoForm()
        ingreso_form = IngresarProductoForm()
        return render(request,self.template_name,locals())
    def post(self,request):
        producto_form = ProductoForm(request.POST)
        ingreso_form = IngresarProductoForm(request.POST)
        if producto_form.is_valid():
            producto = producto_form.save()
            messages.success(request, 'El producto '+str(producto.descripcion)+' de código '+str(producto.codigo)+' fue registrado con exito')
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresarProductoForm()
            return render(request,self.template_name,locals())
        elif(ingreso_form.is_valid()):
            producto = Producto.objects.get(codigo=request.POST['producto'])
            producto.stock_actual += int(request.POST['cantidad'])
            producto.save()
            messages.success(request, 'Se ingresaron '+request.POST['cantidad']+' unidades de '+producto.descripcion)
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresarProductoForm()
            return render(request,self.template_name,locals())
        else:
            messages.error(request, 'No se pudo registrar la operación, porfavor intente denuevo.')
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresarProductoForm()
            return render(request,self.template_name,locals())

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ObtenerProducto(request):
    data = json.loads(request.body)
    lista = []
    productos = Producto.objects.all().exclude(codigo__in=data['productos'])
    for p in productos:
        lista.append({"codigo" : p.codigo, "nombre" : p.descripcion},)
    return HttpResponse(json.dumps(lista),content_type='application/json')

