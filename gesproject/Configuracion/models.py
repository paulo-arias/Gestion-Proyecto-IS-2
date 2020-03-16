from django.db import models

# Create your models here.

class Configuracion(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
