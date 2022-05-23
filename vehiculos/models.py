from django.db import models

from personas.models import Conductor, Usuario

# Create your models here.
class Vehiculo (models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.IntegerField(default=2022)
    marca = models.CharField(max_length=30)
    capacidad = models.IntegerField(default=1)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,blank=True)
    conductor =models.ForeignKey(Conductor,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.placa+" "+str(self.modelo)+" "+self.marca

class Infraccion(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=80)
    valor = models.DecimalField(max_digits=15,decimal_places=2)
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE,null=True,blank=True)
    conductor =  models.ForeignKey(Conductor,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.fecha)+" "+self.descripcion+" "+str(self.valor)