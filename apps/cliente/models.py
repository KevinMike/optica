from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    def __unicode__(self):
        return "%s, %s" (self.nombre,self.apellido)
