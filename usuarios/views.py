from typing import Any, Dict
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth import get_user_model

from .models import Estudiante, Docente, Usuario
from .forms import (EstudianteCrearModelForm, EstudianteEditarModelForm,
                    DocenteCrearModelForm, DocenteEditarModelForm,
                    UsuarioCrearModelForm, UsuarioEditarModelForm)
from .util import generate_password


UsuarioAutenticable = get_user_model()

# -------------------------------------------------------------------
# -----> Vistas módulo Estudiantes


class EstudianteListaView(generic.ListView):
    template_name = 'estudiantes/lista_estudiante.html'
    queryset = Estudiante.objects.all()
    context_object_name = 'estudiantes'


class EstudianteCrearView(generic.CreateView):
    template_name = 'estudiantes/crear_estudiante.html'
    form_class = EstudianteCrearModelForm

    def get_success_url(self):
        return reverse('usuarios:lista-estudiante')

    def form_valid(self, form):
        nuevo_estudiante = form.save(commit=False)
        usuario = nuevo_estudiante.carnet
        password = self.get_context_data()['password']
        nuevo_usuario_autenticable = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_estudiante.usuario_id = nuevo_usuario_autenticable.id
        nuevo_estudiante.save()
        return super(EstudianteCrearView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class EstudianteEditarView(generic.UpdateView):
    template_name = 'estudiantes/editar_estudiante.html'
    queryset = Estudiante.objects.all()
    form_class = EstudianteEditarModelForm

    def get_success_url(self):
        return reverse('usuarios:lista-estudiante')


# -------------------------------------------------------------------
# -----> Vistas módulo Docentes


class DocenteListaView(generic.ListView):
    template_name = 'docentes/lista_docente.html'
    queryset = Docente.objects.all()
    context_object_name = 'docentes'


class DocenteCrearView(generic.CreateView):
    template_name = 'docentes/crear_docente.html'
    form_class = DocenteCrearModelForm

    def get_success_url(self):
        return reverse('usuarios:lista-docente')

    def form_valid(self, form):
        nuevo_docente = form.save(commit=False)
        usuario = nuevo_docente.cui
        password = self.get_context_data()['password']
        nuevo_usuario_autenticable = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_docente.usuario_id = nuevo_usuario_autenticable.id
        nuevo_docente.save()
        return super(DocenteCrearView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class DocenteEditarView(generic.UpdateView):
    template_name = 'docentes/editar_docente.html'
    queryset = Docente.objects.all()
    form_class = DocenteEditarModelForm

    def get_success_url(self):
        return reverse('usuarios:lista-docente')


# -------------------------------------------------------------------
# -----> Vistas módulo Usuarios


class UsuarioListaView(generic.ListView):
    template_name = 'usuarios/lista_usuario.html'
    queryset = Usuario.objects.all()
    context_object_name = 'usuarios'


class UsuarioCrearView(generic.CreateView):
    template_name = 'usuarios/crear_usuario.html'
    form_class = UsuarioCrearModelForm

    def get_success_url(self):
        return reverse('usuarios:lista-usuario')

    def form_valid(self, form):
        nuevo_usuario = form.save(commit=False)
        usuario = nuevo_usuario.cui
        password = self.get_context_data()['password']
        nuevo_usuario_autenticable = UsuarioAutenticable.objects.create(
            username=usuario, password=password)
        nuevo_usuario.usuario_id = nuevo_usuario_autenticable.id
        nuevo_usuario.save()
        return super(UsuarioCrearView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class UsuarioEditarView(generic.UpdateView):
    template_name = 'usuarios/editar_usuario.html'
    queryset = Usuario.objects.all()
    form_class = UsuarioEditarModelForm

    def get_success_url(self):
        return reverse('usuarios:lista-usuario')
