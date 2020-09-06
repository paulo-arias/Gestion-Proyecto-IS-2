from django.db import models


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

    #one to one
    #tarea_padre = models.OneToOneField('self', null=True, blank=True)  # , on_delete=models.CASCADE

    #proyecto
    proyecto = models.ForeignKey('Proyecto', null=True, blank=True, help_text='Proyecto al que pertence', on_delete=models.SET_NULL)  # , on_delete=models.CASCADE

    #linea base
    #linea_base = models.ForeignKey('Configuracion.LineaBase', null=True, blank=True, help_text='Linea Base a la que pertence', on_delete=models.SET_NULL)  # , on_delete=models.CASCADE
    
    #variables para guardar los valores iniciales
    og_version = None
    og_prioridad = None
    og_estado = None
    og_descripcion = None
    og_observacion = None
    og_tareapadre = None
    og_proyecto = None
    og_request = None

    def __init__(self, *args, **kwargs):
        super(Tarea, self).__init__(*args, **kwargs)
        #guardamos los valores inicales
        self.og_version = self.version
        self.og_prioridad = self.prioridad
        self.og_estado = self.estado
        self.og_descripcion = self.descripcion
        self.og_observacion = self.observacion
        self.og_tareapadre = self.version
        self.og_proyecto = self.version
        
    #def save(self, *args, **kwargs):
    #   if self.linea_base:
    #        if (self.og_version != self.version) or (self.og_prioridad != self.prioridad) or (self.og_estado != self.estado) or (self.og_descripcion != self.descripcion) or (self.og_observacion != self.observacion) or (self.og_tareapadre != self.version) or (self.og_proyecto != self.version):
    #            #messages.warning('POST', 'Tarea en Linea base no!')
    #            raise Exception("Tarea en Linea base no puede ser modificada")
    #        else:
    #            super(Tarea, self).save(*args, **kwargs)
    #    else:
    #        super(Tarea, self).save(*args, **kwargs)
    
    def __str__(self):
        # Al hacer el get de la tarea despliega su descripción
        return 'Nombre: ' + self.descripcion + ', Estado: '+ self.estado + ', Version: ' + self.version


