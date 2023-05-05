from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, reverse
from .forms import CustomeCreationEdificioForm
from django.http import HttpResponse

# Create your views here.

#Validar esta view para
class EdificioView(generic.CreateView):
    template_name = "edificio/edificioCrear.html"
    form_class = CustomeCreationEdificioForm

    def get_success_url(self):
        return reverse('edificio')

def EdificioPage(request):
    return render(request, 'edificio/edificio.html')

def EdificioCrearPage(request):
    return render(request, 'edificio/edificioCrear.html')

def EdificioEditarPage(request):
    return render(request, 'edificio/edificioEditar.html')

def EdificioSalonesPage(request):
    return render(request, 'edificio/salones/salones.html')

def EdificioSalonesCrearPage(request):
    return render(request, 'edificio/salones/salonesCrear.html')

def EdificioSalonesEditarPage(request):
    return render(request, 'edificio/salones/salonesEditar.html')

def EdificioSalonesClasificacionPage(request):
    return render(request, 'edificio/salones/salonesClasificacion.html')

def EdificioSalonesClasificacionCrearPage(request):
    return render(request, 'edificio/salones/salonesClasificacionCrear.html')

def EdificioSalonesClasificacionEditarPage(request):
    return render(request, 'edificio/salones/salonesClasificacionEditar.html')
