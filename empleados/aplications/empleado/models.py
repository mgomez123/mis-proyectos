from django.db import models
from aplications.departamento.models import Departamento
# Create your models here. te arma la base de datos----> object relational map
#acá adentro va solo código pyhton, nada de sql

#creamos una pequeña tabla de base de datos
#1ero creamos-----> titulo charfiled string
#---------------->subtitulo charfield string
#dentro de "models" tiene otra clase Model--->charfield es=varchar
class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

class Meta:
            verbose_name = "Habilidad"
            verbose_name_plural = "Habilidades del empleado"
            ordering=["habilidad"]
            unique_together = ("habilidad",)
            
def __str__(self):
    return self.habilidad 

class Empleado (models.Model):
    JOB_CHOICES =(
    ("0", "CONTADOR"),
    ("1", "ADMINISTRATIVO"),
    ("2", "DESARROLLADOR"),
    ("3", "ANALISTA FUNCIONAL"),
    ("4", "OTRO"),
    )
    
    nombre = models.CharField("Nombre", max_length=60)
    apellido = models.CharField("Apellido", max_length=60)
    trabajo = models.CharField("Puesto", max_length=1,choices= JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    
    class Meta:
        verbose_name_plural = "Empleados"
        ordering=["nombre"]
        
    def __str__(self):
        return self.nombre + "-" + self.apellido 


