from django.db import models
from apps.cliente.models import *
from apps.almacen.models import *
from apps.receta.models import *
# Create your models here.
class Venta(models.Model):
    nro = models.IntegerField(primary_key=True)
    dni_cliente = models.ForeignKey(Cliente,blank=True, null=True)
    fecha = models.DateField()
    subtotal = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.nro

class DetalleVenta(models.Model):
    nro_venta = models.ForeignKey(Venta, primary_key=True)
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True)
    id_receta = models.ForeignKey(Receta, unique=True, blank=True, null=True)
    cantidad = models.IntegerField()


