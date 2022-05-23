from django.contrib import admin
from vehiculos.models import Vehiculo,Infraccion
# Register your models here.

class VehiculoAdmin (admin.ModelAdmin):
    list_display=('placa','modelo','marca','capacidad')
    list_filter=('marca','modelo',)
    search_fields=('placa','marca',)
admin.site.register(Vehiculo,VehiculoAdmin) 

class InfraccionAdmin (admin.ModelAdmin):
    list_display=('fecha','descripcion','valor')
    list_filter=('fecha',)
    search_fields=('fecha','descripcion',)
admin.site.register(Infraccion,InfraccionAdmin) 