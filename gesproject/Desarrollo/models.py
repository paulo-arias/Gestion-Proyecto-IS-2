from django.db import models

# Create your models here.
class Tarea(models.Model):
    version = models.CharField(max_length=255)
    prioridad = models.CharField(max_length=255)

    estados_tarea = (
        ('i', 'Iniciado'),
        ('p', 'Pendiente'),
        ('f', 'Finalizado')
    )

    #estado = models.CharField(max_length=255) # las opciones son [iniciado, pendiente, finalizado]

    estado = models.CharField(max_length=1, choices=estados_tarea, blank=True, default='p', help_text='Estados de la Tarea')

    descripcion = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255)
    #id_tarea_padre = models.CharField(max_length=255) # Se estara viendo con la base de datos

class Proyecto(models.Model):
    Nombre = models.CharField(max_length=255)
    Estado = models.CharField(max_length=255)
