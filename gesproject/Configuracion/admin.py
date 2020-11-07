from django.contrib import admin
from .models import Configuracion, LineaBase
# Register your models here.

from Desarrollo.models import Tarea

@admin.register(Configuracion)
# Se crea una clase que extienda del admin.ModelAdmin
class ConfigAdmin(admin.ModelAdmin):
    list_display = (id,'nombre','apellido')


class TareaInline(admin.StackedInline):
    model = Tarea #tarea.estado?
    fields = ('version', 'estado', 'descripcion')
    #readonly_fields = ('version', 'estado', 'descripcion')
    can_delete = False


@admin.register(LineaBase)
class LineaBaseAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'Nombre', 'Estado') #(id, 'Nombre', 'Estado')
    inlines = [TareaInline,]



