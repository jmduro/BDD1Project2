from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, reverse
from .forms import (EdificioCreateForm, EdificioUpdateForm, 
                    SalonCreateForm, SalonUpdateForm, 
                    SalonClasiCreateForm, SalonClasiUpdateForm)
from .models import Edificio, Salon, Salon_clasificacion


# Create your views here.

# Vistas para Edificio
class EdificioView(generic.ListView):
    template_name = 'edificio/edificio.html'
    queryset = Edificio.objects.all()
    context_object_name = 'edificios'


class EdificioCrearView(generic.CreateView):
    template_name = 'edificio/edificioCrear.html'
    form_class = EdificioCreateForm

    def get_success_url(self):
        return reverse('edificios:edificio')
    
    def form_valid(self, form):
        nuevo_edificio = form.save(commit=False)
        nuevo_edificio.save()
        return super(EdificioCrearView, self).form_valid(form)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context

class EdificioEditarView(generic.UpdateView):
    template_name = 'edificio/edificioEditar.html'
    queryset = Edificio.objects.all()
    form_class = EdificioUpdateForm

    def get_success_url(self):
        return reverse('edificios:edificio')

# Vistas para Salon

class SalonesView(generic.ListView):
    template_name = 'salones/salones.html'
    queryset = Salon.objects.all()
    context_object_name = 'salones'


class SalonesCrearView(generic.CreateView):
    template_name = 'salones/salonesCrear.html'
    form_class = SalonCreateForm

    def get_success_url(self):
        return reverse('edificios:salones')
    
    def form_valid(self, form):
        nuevo_salon = form.save(commit=False)
        nuevo_salon.save()
        return super(SalonCreateForm, self).form_valid(form)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context

class SalonesEditarView(generic.UpdateView):
    template_name = 'edificio/salones/salonesEditar.html'
    queryset = Salon.objects.all()
    form_class = SalonUpdateForm

    def get_success_url(self):
        return reverse('edificios:salones')

# Vistas para Clasificacion Salon

class SalonesClasificacionView(generic.ListView):
    template_name = 'clasificacion/salonesClasificacion.html'
    queryset = Salon_clasificacion.objects.all()
    context_object_name = 'clasificacionSalones'

class SalonesClasificacionCrearView(generic.CreateView):
    template_name = 'clasificacion/salonesClasificacionCrear.html'
    form_class = SalonClasiCreateForm

    def get_success_url(self):
        return reverse('edificios:clasificacionSalones')
    
    def form_valid(self, form):
        nueva_clasi = form.save(commit=False)
        nueva_clasi.save()
        return super(SalonesClasificacionCrearView, self).form_valid(form)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context

class SalonesClasificacionEditarView(generic.UpdateView):
    template_name = 'clasificacion/salonesClasificacionEditar.html'
    queryset = Salon_clasificacion.objects.all()
    form_class = SalonClasiUpdateForm

    def get_success_url(self):
        return reverse('edificios:clasificacionSalones')