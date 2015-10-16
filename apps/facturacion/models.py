# -*- encoding: utf-8 -*-
from django.db import models
from apps.cliente.models import *
from apps.almacen.models import Producto
from apps.receta.models import *
from django.utils import timezone
# Create your models here

class Venta(models.Model):
    nro = models.IntegerField(primary_key=True)
    dni_cliente = models.ForeignKey(Cliente,blank=True, null=True)
    fecha = models.DateField(default = timezone.now())
    subtotal = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    cancelado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

class DetalleVenta(models.Model):
    nro_venta = models.ForeignKey(Venta,blank=True)
    producto = models.ForeignKey(Producto)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)

class Aditivos(models.Model):
    componente = models.CharField(max_length=30)
    def __unicode__(self):
        return self.componente
class Lente(models.Model):
    tipo_lente = models.CharField(max_length=30)
    def __unicode__(self):
        return self.tipo_lente

class DetalleLente(models.Model):
    LENTES = (
        ('0','Seleccione un tipo de lente'),
        ('1','Lente Monofocal'),
        ('2','Lente Bifocal'),
        ('3','Lente Multifocal'),
        ('4','Lente de Contacto'),
    )
    #lente = models.CharField(max_length="1",choices=LENTES)
    nro_venta = models.OneToOneField(Venta, primary_key=True)
    lente = models.ForeignKey(Lente)
    complementos = models.ManyToManyField(Aditivos)
    precio = models.IntegerField(default=0)

class NotaPedido(models.Model):
    venta = models.ForeignKey(Venta)
    fecha = models.DateField(default=timezone.now())
    importe = models.IntegerField(default=0)
    saldo = models.IntegerField(default=0)
