from django.contrib import admin
from reparaciones.models import Reparacion,Detalle,Servicio
# Register your models here.

# class ReparacionAdmin (admin.ModelAdmin):
#     list_display=('fecha','costo','descripcion')
#     list_filter=('fecha','costo',)
#     search_fields=('fecha','descripcion',)
# admin.site.register(Reparacion,ReparacionAdmin) 

class DetalleAdmin(admin.ModelAdmin):
    list_display=('costo','servicio')
    list_filter=('servicio',)
    search_fields=('costo','servicio',)
admin.site.register(Detalle,DetalleAdmin)    

class ServicioAdmin(admin.ModelAdmin):
    list_display=('precio','descripcion')
    list_filter=('precio','descripcion',)
    search_fields=('precio','descripcion',)
admin.site.register(Servicio,ServicioAdmin)    

# para que salga el formulario maestro detalle
# admin.StackedInline
#admin.TabularInline
class detalle_reparacion(admin.TabularInline):
    model=Detalle

class ReparacionAdmin(admin.ModelAdmin):
    list_display=('fecha','costo','descripcion','vehiculo')
    list_filter=('fecha','costo',)
    search_fields=('fecha','descripcion',)
    inlines=(detalle_reparacion,)

admin.site.register(Reparacion,ReparacionAdmin) 
