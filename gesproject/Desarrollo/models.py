from django.db import models

from Configuracion.models import LineaBase

class Proyecto(models.Model):
    Nombre = models.CharField(max_length=255)
    Estado = models.CharField(max_length=255)

    def __str__(self):
        return self.Nombre

class Tarea(models.Model):

    #el id es automaticamente por django
    #id = models.Integerfield(primary_key = true) #si le quiero poner

    version = models.CharField(max_length=255)
    prioridad = models.CharField(max_length=255)

    estados_tarea = (
        ('i', 'Iniciado'),
        ('p', 'Pendiente'),
        ('f', 'Finalizado')
    )

    estado = models.CharField(max_length=1, choices=estados_tarea, blank=True, default='p', help_text='Estados de la Tarea')

    descripcion = models.CharField(max_length=255, null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    #fecha creacion? fecha_Creacion = models.Datefield()

    #id_tarea_padre
    tarea_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL) #, on_delete=models.CASCADE

    #proyecto
    proyecto = models.ForeignKey('Proyecto', null=True, blank=True, help_text='Proyecto al que pertence', on_delete=models.SET_NULL)  # , on_delete=models.CASCADE

    linea base
    linea_base = models.ForeignKey('Configuracion.LineaBase', null=True, blank=True, help_text='Linea Base a la que pertence', on_delete=models.SET_NULL)  # , on_delete=models.CASCADE


    def __str__(self):
        # Al hacer el get de la tarea despliega su descripción
        return 'Nombre: ' + self.descripcion + ', Estado: '+ self.estado + ', Version: ' + self.version


