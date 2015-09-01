from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    def __unicode__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, blank=True, null=True)
    longitud = models.CharField(max_length=15, blank=True, null=True)
    precio_sugerido = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.descripcion

class Almacen(models.Model):
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True)
    stock = models.SmallIntegerField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)





class ProductoProveedor(models.Model):
    codigo_producto = models.ForeignKey(Producto)
    id_proveedor = models.ForeignKey(Proveedor)


