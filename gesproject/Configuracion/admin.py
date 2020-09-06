from django.contrib import admin
from .models import Configuracion
from .models import LineaBase
# Register your models here.

#@admin.register(Configuracion)
# Se crea una clase que extienda del admin.ModelAdmin
#class ConfigAdmin(admin.ModelAdmin):
#   list_display = (id,'nombre','apellido')

@admin.register(LineaBase)

class LineaBaseAdmin(admin.ModelAdmin):
    list_display = (id,'Codigo','Nombre')