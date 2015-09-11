from django.contrib import admin
from .forms import *
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ('nombre','descripcion',)
    search_fields = ('nombre',)
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ('nombre','telefono','observaciones')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('codigo','descripcion','marca','color','categoria','longitud','stock_actual')
    list_filter = ('categoria','marca','color',)
    search_fields = ('descripcion',)
    exclude = ('stock_actual',)

# @admin.register(Almacen)
# class AlmacenAdmin(admin.ModelAdmin):
#     model = Almacen
#     list_display = ('codigo_producto','stock','observacion',)