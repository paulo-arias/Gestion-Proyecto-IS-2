from django.db import models

# Create your models here.

class Configuracion(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)


class LineaBase(models.Model):
    Codigo = models.IntegerField(primary_key=True)  # si le quiero poner
    Nombre = models.CharField(max_length=255)

    estados_lb = (
        ('i', 'Iniciado'),
        ('p', 'Pendiente'),
        ('f', 'Finalizado')
    )

    Estado = models.CharField(max_length=1, choices=estados_lb, blank=True, default='p', help_text='Estados de la Tarea')

    def __str__(self):
        return self.Nombre