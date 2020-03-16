from django.db import models

# Create your models here.
class Desarrollo(models.Model):
    tarea = models.CharField(max_length=255)
    proyecto = models.CharField(max_length=255)
