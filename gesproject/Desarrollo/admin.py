from django.contrib import admin
from .models import Tarea
from .models import Proyecto#, LineaBase
#from .models import Proyecto, Tarea


@admin.register(Tarea)
# Se crea una clase que extienda del admin.ModelAdmin
class TareaAdmin(admin.ModelAdmin):
    list_display = (id,'version','prioridad','estado','descripcion','observacion')

    #def has_change_permission(self, request, obj=None):
     #   if obj:
      #      lb = obj.linea_base
       #     if lb:
        #        return False

        #return super().has_change_permission(request, obj=obj)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            lb = obj.linea_base
            if lb:
                return ['version','prioridad','estado','descripcion','observacion','tarea_padre','proyecto']
        return super().get_readonly_fields(request, obj)


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = (id,'Nombre','Estado')



