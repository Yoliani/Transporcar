from django.contrib import admin
from personas.models import Usuario,Conductor
# Register your models here.

class UsuarioAdmin (admin.ModelAdmin):
    list_display=('documento','nombres','apellidos','direccion','telefono','correo')
    list_filter=('apellidos',)
    search_fields=('nombres','apellidos',)
admin.site.register(Usuario,UsuarioAdmin)  

class ConductorAdmin (admin.ModelAdmin):
    list_display=('documento','nombres','apellidos','direccion','telefono','correo')
    list_filter=('apellidos',)
    search_fields=('nombres','apellidos',)
admin.site.register(Conductor,ConductorAdmin)  


