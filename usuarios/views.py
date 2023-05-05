from typing import Any, Dict
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth import get_user_model

from .models import Estudiante, Docente
from .forms import (EstudianteCreateModelForm, EstudianteUpdateModelForm,
                    DocenteCreateModelForm, DocenteUpdateModelForm)
from .util import generate_password


UsuarioAutenticable = get_user_model()

# -------------------------------------------------------------------
# -----> Vistas módulo Estudiantes


class EstudianteListView(generic.ListView):
    template_name = 'estudiantes/estudiante_list.html'
    queryset = Estudiante.objects.all()
    context_object_name = 'estudiantes'


class EstudianteCreateView(generic.CreateView):
    template_name = 'estudiantes/estudiante_create.html'
    form_class = EstudianteCreateModelForm

    def get_success_url(self):
        return reverse('usuarios:estudiante-list')

    def form_valid(self, form):
        nuevo_estudiante = form.save(commit=False)
        usuario = nuevo_estudiante.carnet
        password = self.get_context_data()['password']
        nuevo_usuario = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_estudiante.usuario_id = nuevo_usuario.id
        nuevo_estudiante.save()
        return super(EstudianteCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class EstudianteUpdateView(generic.UpdateView):
    template_name = 'estudiantes/estudiante_update.html'
    queryset = Estudiante.objects.all()
    form_class = EstudianteUpdateModelForm

    def get_success_url(self):
        return reverse('usuarios:estudiante-list')


# -------------------------------------------------------------------
# -----> Vistas módulo Docentes


class DocenteListView(generic.ListView):
    template_name = 'docentes/docente_list.html'
    queryset = Docente.objects.all()
    context_object_name = 'docentes'


class DocenteCreateView(generic.CreateView):
    template_name = 'docentes/docente_create.html'
    form_class = DocenteCreateModelForm

    def get_success_url(self):
        return reverse('usuarios:docente-list')

    def form_valid(self, form):
        nuevo_docente = form.save(commit=False)
        usuario = nuevo_docente.cui
        password = self.get_context_data()['password']
        nuevo_usuario = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_docente.usuario_id = nuevo_usuario.id
        nuevo_docente.save()
        return super(DocenteCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class DocenteUpdateView(generic.UpdateView):
    template_name = 'docentes/docente_update.html'
    queryset = Docente.objects.all()
    form_class = DocenteUpdateModelForm

    def get_success_url(self):
        return reverse('usuarios:docente-list')


# -------------------------------------------------------------------
# -----> Vistas módulo Usuarios
