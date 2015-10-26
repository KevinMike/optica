from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseBadRequest
from apps.usuarios.views import LoginRequiredMixin
from apps.receta.models import Receta
from apps.facturacion.models import Venta
from .models import Cliente
from .forms import ClienteForm
import json
# Create your views here.

class Index(LoginRequiredMixin, View):
    template_name = 'clientes/index.html'
    def get(self,request):
        ventas = Venta.objects.all()
        recetas = Receta.objects.all()
        return render(self.request,self.template_name,locals())


@csrf_exempt
def SaveClient(request):
    print "request nuevo!!!"
    template_name = 'facturacion/index.html'
    if request.method == 'POST':
        if request.is_ajax():
            data = json.loads(request.body)
            cliente_form = ClienteForm(data)
            if (cliente_form.is_valid()):
                print "formulario valido  :D"
                cliente_form.save()
                mensaje = {'mensaje':'El cliente ' + str(data['nombre']) + ' '+ str(data['apellido']) +' fue registrado con exito','datos': data }
                return  HttpResponse(json.dumps(mensaje),content_type='application/json')
            else:
                print "formulario invalido  :("
                errores = {}
                if cliente_form.errors:
                    for e in cliente_form.errors:
                        errores[e] = unicode(cliente_form.errors[e])
                    mensaje = {'mensaje':'No se pudo registrar al cliente, corrija los errores.','errores':errores }
                    return HttpResponseBadRequest(json.dumps(mensaje),content_type='application/json')
        else:
            print "Request no ajax :o"
            cliente_form = ClienteForm(request.POST,request.FILES)
            if cliente_form.is_valid():
                print "formulario valido  :D"
                cliente_form.save()
                return redirect('/facturacion/')
            else:
                print "formulario invalido  :("
                return render(request,template_name,locals())
    else:
        return redirect('/facturacion/')

def SearchClient(request,cliente_id):
    lista = []
    cliente = Cliente.objects.get(pk=cliente_id)
    if cliente.dni==cliente_id:
        lista.append(
            {
                'foto':cliente.fotografia(),
                'nombre':cliente.nombre + ' '+cliente.apellido,
                'telefono':cliente.telefono,
                'email':cliente.email,
             })
    else:
        lista.append(
            {
                'Mensaje':'Cliente no encontrado',
             })
    return HttpResponse(json.dumps(lista),content_type='application/json')