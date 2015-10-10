from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Venta)
class ClienteAdmin(admin.ModelAdmin):
    model = Venta
    list_display =  ('nro','dni_cliente','fecha','subtotal','total',)
    search_fields = ('nro',)