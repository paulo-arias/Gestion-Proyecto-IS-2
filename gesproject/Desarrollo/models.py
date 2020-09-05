from django.db import models


class Proyecto(models.Model):
    Nombre = models.CharField(max_length=255)
    Estado = models.CharField(max_length=255)


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

    #one to one
    #tarea_padre = models.OneToOneField('self', null=True, blank=True)  # , on_delete=models.CASCADE

    #proyecto
    proyecto = models.ForeignKey('Proyecto', null=True, blank=True, help_text='Proyecto al que pertence', on_delete=models.SET_NULL)  # , on_delete=models.CASCADE

    #linea base
    linea_base = models.ForeignKey('LineaBase', null=True, blank=True, help_text='Linea Base a la que pertence', on_delete=models.SET_NULL)  # , on_delete=models.CASCADE


class LineaBase(models.Model):
    Codigo = models.Integerfield(primary_key=True)  # si le quiero poner
    Nombre = models.CharField(max_length=255)

    estados_lb = (
        ('i', 'Iniciado'),
        ('p', 'Pendiente'),
        ('f', 'Finalizado')
    )

    Estado = models.CharField(max_length=1, choices=estados_lb, blank=True, default='p', help_text='Estados de la Tarea')
