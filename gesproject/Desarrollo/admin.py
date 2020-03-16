from django.contrib import admin
from .models import Desarrollo
# Register your models here.
@admin.register(Desarrollo)
# Se crea una clase que extienda del admin.ModelAdmin
class DesarrolloAdmin(admin.ModelAdmin):
    list_display = (id,'tarea','proyecto')
