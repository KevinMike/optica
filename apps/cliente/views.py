from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseBadRequest
from .models import Cliente
from .forms import ClienteForm
import json
from django.views.decorators.csrf import csrf_exempt
from apps.facturacion.forms import *
# Create your views here.
@csrf_exempt
def SaveClient(request):
    print "request nuevo!!!"
    template_name = 'facturacion/index.html'
    if request.method == 'POST':
        if request.is_ajax():
            print "es ajax yupiii"
            data = json.loads(request.body)
            # if  data['foto'] == '':
            #     data['foto'] = 'pic_folder/default_user.png'
            print data
            cliente_form = ClienteForm(data)
            if (cliente_form.is_valid()):
                print "formulario valido  :D"
                cliente_form.save()
                mensaje = "El cliente fue registrado con exito"
                return  HttpResponse(json.dumps(mensaje),content_type='application/json')
            else:
                print "formulario invalido  :("
                errores = {}
                if cliente_form.errors:
                    for e in cliente_form.errors:
                        errores[e] = unicode(cliente_form.errors[e])
                    lista = json.dumps(errores)
                    print lista
                    return HttpResponse(lista,content_type='application/json')
        else:
            print "Request no ajax :o"
            cliente_form = ClienteForm(request.POST,request.FILES)
            if cliente_form.is_valid():
                print "formulario valido  :D"
                cliente_form.save()
                return redirect('/')
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