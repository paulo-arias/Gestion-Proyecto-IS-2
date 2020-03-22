from django.contrib import admin
from .models import Tarea
from .models import Proyecto

# Register your models here.
@admin.register(Tarea)

# Se crea una clase que extienda del admin.ModelAdmin
class TareaAdmin(admin.ModelAdmin):
    list_display = (id,'version','prioridad','estado','descripcion','observacion')

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = (id,'Nombre','Estado')
