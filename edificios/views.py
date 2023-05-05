from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, reverse
from .forms import (EdificioCreateForm, )
from .models import Edificio, Salon, Salon_clasificacion


# Create your views here.

# Vistas para Edificio
class EdificioView(generic.ListView):
    template_name = 'edificio/edificio.html'
    queryset = Edificio.objects.all()
    context_object_name = 'edificio'


class EdificioCrearView(generic.CreateView):
    template_name = 'edificio/edificioCrear.html'
    form_class = EdificioCreateForm




class EdificioEditarView(generic.UpdateView):
    template_name = 'edificio/edificioEditar.html'
    queryset = Edificio.objects.all()
    #form_class = EdificioUpdateForm

    

# Vistas para Salon

class SalonesView(generic.ListView):
    template_name = 'salones/salones.html'
    queryset = Salon.objects.all()
    context_object_name = 'salones'


class SalonesCrearView(generic.CreateView):
    template_name = 'salones/salonesCrear.html'

class SalonesEditarView(generic.UpdateView):
    template_name = 'edificio/salones/salonesEditar.html'

# Vistas para Clasificacion Salon

class SalonesClasificacionView(generic.ListView):
    template_name = 'clasificacion/salonesClasificacion.html'
    queryser = Salon_clasificacion.objects.all()
    context_object_name = 'salonesClasificacion'

class SalonesClasificacionCrearView(generic.CreateView):
    template_name = 'clasificacion/salonesClasificacionCrear.html'

class SalonesClasificacionEditarView(generic.UpdateView):
    template_name = 'clasificacion/salonesClasificacionEditar.html'
