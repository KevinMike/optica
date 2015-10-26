# -*- encoding: utf-8 -*-
from django.db import models
from apps.cliente.models import *
from apps.almacen.models import Producto,Lente,Aditivos
from apps.receta.models import *
from django.utils import timezone
# Create your models here

class Venta(models.Model):
    nro = models.IntegerField(primary_key=True)
    dni_cliente = models.ForeignKey(Cliente,blank=True, null=True)
    fecha = models.DateField(default = timezone.now())
    importe = models.IntegerField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    cancelado = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "Venta nro. %i" %(self.nro)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class DetalleVenta(models.Model):
    nro_venta = models.ForeignKey(Venta,blank=True)
    producto = models.ForeignKey(Producto,blank=True, null=True)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    def __unicode__(self):
        return "%s - %s" %(self.producto,self.cantidad)

class DetalleLente(models.Model):
    nro_venta = models.OneToOneField(Venta, blank=True)
    lente = models.ForeignKey(Lente)
    complementos = models.ManyToManyField(Aditivos)
    precio = models.IntegerField(default=0)

class NotaPedido(models.Model):
    venta = models.ForeignKey(Venta)
    fecha = models.DateField(default=timezone.now())
    importe = models.IntegerField(default=0)
    saldo = models.IntegerField(default=0)

    def __unicode__(self):
        return "Nota de Pedido nro. %i" %(self.id)

    class Meta:
        verbose_name = 'Nota de Pedido'
        verbose_name_plural = 'Notas de Pedido'

