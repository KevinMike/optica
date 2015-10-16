from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Aditivos)
class AditivosAdmin(admin.ModelAdmin):
    model = Aditivos
    list_display =  ('componente',)

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    model = Venta
    inline = [DetalleVentaInline,]



