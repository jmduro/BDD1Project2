from typing import Any, Dict
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth import get_user_model

from .models import Estudiante
from .forms import EstudianteCreateModelForm, EstudianteUpdateModelForm
from .util import generate_password

UsuarioAutenticable = get_user_model()

# Vistas módulo Estudiantes

class EstudianteListView(generic.ListView):
    template_name = 'estudiantes/estudiante_list.html'
    queryset = Estudiante.objects.all()
    context_object_name = 'estudiantes'


class EstudianteDetailView(generic.DetailView):
    template_name = 'estudiantes/estudiante_detail.html'
    queryset = Estudiante.objects.all()
    context_object_name = 'estudiante'


class EstudianteCreateView(generic.CreateView):
    template_name = 'estudiantes/estudiante_create.html'
    form_class = EstudianteCreateModelForm

    def get_success_url(self):
        return reverse('usuarios:estudiante-list')

    def form_valid(self, form):
        nuevo_estudiante = form.save(commit=False)
        usuario = nuevo_estudiante.carnet
        password = self.get_context_data()['password']
        nuevo_usuario = UsuarioAutenticable.objects.create(username=usuario, password=password)
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


class EstudianteDeleteView(generic.DeleteView):
    template_name = 'estudiantes/estudiante_delete.html'
    queryset = Estudiante.objects.all()

    def get_success_url(self):
        return reverse('usuarios:estudiante-list')


# Vistas módulo Docentes

# Vistas módulo Usuarios