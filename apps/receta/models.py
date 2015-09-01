from django.db import models
from apps.cliente.models import *
# Create your models here.

class Receta(models.Model):
    dni_cliente = models.ForeignKey(Cliente,blank=True, null=True)
    fecha = models.DateField()
    imagen = models.BinaryField()
    def __unicode__(self):
        return  "%s - %d" (self.dni_cliente,self.fecha)