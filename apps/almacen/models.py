from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    productos = models.ManyToManyField("Producto")
    observaciones = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "PROVEEDORES"


class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "CATEGORIAS"

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True)
    longitud = models.CharField(max_length=15, blank=True, null=True)
    precio_sugerido = models.IntegerField(blank=True, null=True,default=0)
    stock_minimo = models.IntegerField(blank=True, null=True,default=0)
    stock_actual = models.IntegerField(blank=True,null=True,default=0)
    def __unicode__(self):
        return "%s - %s" %(self.codigo, self.descripcion )
    class Meta:
        verbose_name_plural = "PRODUCTOS"


