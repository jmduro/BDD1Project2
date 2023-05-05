from typing import Any, Dict
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth import get_user_model

from .models import Estudiante
from .forms import EstudianteCreateModelForm, EstudianteUpdateModelForm
from .util import generate_password

UsuarioAutenticable = get_user_model()


class EstudianteListView(generic.ListView):
    template_name = 'estudiantes/estudiante_list.html'
    queryset = Estudiante.objects.all()
    context_object_name = 'estudiantes'


class EstudianteDetailView(generic.DetailView):
    template_name = 'estudiantes/estudiante_detail.html'
    queryset = Estudiante.objects.all()
    context_object_name = 'estudiante'


class EstudianteCreateView(generic.CreateView):
    template_name = 'estudiantes/estudiante-create.html'
    form_class = EstudianteCreateModelForm
    usuario_global = ''
    password_global = ''

    def get_success_url(self):
        return reverse('estudiantes:estudiante-list')

    def form_valid(self, form):
        estudiante = form.save(commit=False)
        usuario = estudiante.carnet
        password = self.get_context_data()['password']
        UsuarioAutenticable.objects.create(usuario=usuario, password=password)
        estudiante.save()
        return super(EstudianteCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        password = generate_password()
        context.update({'password': password})
        return context


class EstudianteUpdateView(generic.CreateView):
    template_name = 'estudiantes/estudiante-update.html'
    queryset = Estudiante.objects.all()
    form_class = EstudianteUpdateModelForm

    def get_success_url(self):
        return reverse('estudiantes:estudiante-list')


class EstudianteDeleteView(generic.DeleteView):
    template_name = 'estudiantes/estudiante-delete.html'
    queryset = Estudiante.objects.all()

    def get_success_url(self):
        return reverse('estudiantes:estudiante-list')
