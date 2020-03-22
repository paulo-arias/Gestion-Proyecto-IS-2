from django.db import models

# Create your models here.
class Tarea(models.Model):
    version = models.CharField(max_length=255)
    prioridad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255) # las opciones son [iniciado, pendiente, finalizado]
    descripcion = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255)
    #id_tarea_padre = models.CharField(max_length=255) # Se estara viendo con la base de datos

class Proyecto(models.Model):
    Nombre = models.CharField(max_length=255)
    Estado = models.CharField(max_length=255)
