from typing import Any, Dict
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth import get_user_model

from .models import Estudiante, Docente, Usuario
from .forms import (EstudianteCreateModelForm, EstudianteUpdateModelForm,
                    DocenteCreateModelForm, DocenteUpdateModelForm,
                    UsuarioCreateModelForm, UsuarioUpdateModelForm)
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
        nuevo_usuario_autenticable = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_estudiante.usuario_id = nuevo_usuario_autenticable.id
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
        nuevo_usuario_autenticable = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_docente.usuario_id = nuevo_usuario_autenticable.id
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


class UsuarioListView(generic.ListView):
    template_name = 'usuarios/usuario_list.html'
    queryset = Usuario.objects.all()
    context_object_name = 'usuarios'


class UsuarioCreateView(generic.CreateView):
    template_name = 'usuarios/usuario_create.html'
    form_class = UsuarioCreateModelForm

    def get_success_url(self):
        return reverse('usuarios:usuario-list')

    def form_valid(self, form):
        nuevo_usuario = form.save(commit=False)
        usuario = nuevo_usuario.cui
        password = self.get_context_data()['password']
        nuevo_usuario_autenticable = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_usuario.usuario_id = nuevo_usuario_autenticable.id
        nuevo_usuario.save()
        return super(UsuarioCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class UsuarioUpdateView(generic.UpdateView):
    template_name = 'usuarios/usuario_update.html'
    queryset = Usuario.objects.all()
    form_class = UsuarioUpdateModelForm

    def get_success_url(self):
        return reverse('usuarios:usuario-list')
