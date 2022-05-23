from django.shortcuts import render
from reparaciones.models import Servicio, Vehiculo
from django.contrib.auth.decorators import login_required
#======== para el PDF=============================
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa 
from django.template.loader import get_template
#=================================================

# Create your views here.

#Crear una vista para el listado de vehiculos
def lista_vehiculo(request):
    vehiculos=Vehiculo.objects.all() # select * from vehiculos
    data={'vehiculos':vehiculos}
    return render(request,'lista_vehiculo.html',data)

def index(request):
        return render(request,'index.html')
        
#==-------- meteodo para recibir los datos y guardar un servicio=========
@login_required(login_url='/account/login/')
def registrar_servicios(request):
     data={}
     if request.method == 'POST':
         servicio=Servicio()#crea un obj de servcicio
         descripcion=request.POST.get('descripcion')#captura del formulario la decrip
         precio=request.POST.get('precio')#captura del formulario el precio
         #-------- mete en el obj lo recibido-------
         servicio.descripcion=descripcion
         servicio.precio=precio
         #----------------------------------------
         #---- Guarda en la bd el servicio
         servicio.save()
         data={'msg':'Registro Guardado correctamente'}
         print('registro guardado correctamente')# muestra en consoloa
     return render(request,'servicios.html',data)
#===  Eliminar un vehiculo====================
#/delete-vehiculo/2

def delete_vehiculo(request,id):
    vehiculo=Vehiculo.objects.get(id=id)
    placa=vehiculo.placa
    vehiculo.delete()
    
    vehiculos=Vehiculo.objects.all() # select * from vehiculos
    data={'vehiculos':vehiculos,'msg':'Registro eliminado con éxito! '+placa}
    return render(request,'lista_vehiculo.html',data)
#----------- pdf*---------------------------------------
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
#----------------------------------------------------------------------------
def listado_pdf(request):
     vehiculos = Vehiculo.objects.all()
     data={'vehiculos':vehiculos}
     pdf = render_to_pdf('vehiculos_pdf.html', data)
     return HttpResponse(pdf, content_type='application/pdf')
