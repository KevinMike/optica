from django.contrib import admin
from .models import Receta
# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    model = Receta
    list_display = ('id','cliente','fecha')

admin.site.register(Receta,RecetaAdmin)