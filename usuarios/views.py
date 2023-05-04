from django.shortcuts import render, reverse
from django.views import generic

from .models import Estudiante
from .forms import EstudianteCreateModelForm, EstudianteUpdateModelForm


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

    def get_success_url(self):
        return reverse('estudiantes:estudiante-list')


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
