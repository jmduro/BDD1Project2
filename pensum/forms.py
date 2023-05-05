from django import forms
from .models import Carrera, Curso, Pensum, Ciclo, CursoPensum

class CarreraModelForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = (
            'nombre',
            'duracion',
            'clasificacion',
            'partida',
            'ciclo_academico',
            'grado_academico',
            'jornada',
            #'encargado_area',
            #'coordinador_academico',
            'habilitado',
        )

class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = (
            'codigo',
            'nombre',
            'horas_semana',
            'carrera',
            'laboratorio',
            'codigo_lab',
            'horas_lab',
            'semestres',
            'habilitado',
        )

class PensumModelForm(forms.ModelForm):
    class Meta:
        model = Pensum
        fields = (
            'codigo',
            'inicio',
            'creacion',
            'proceso',
            'ciclos',
            'examen',
            'habilitado',
            'carrera', 
        )

class CicloModelForm(forms.ModelForm):
    class Meta:
        model = Ciclo
        fields = (
            'pensum',
            'ciclo'
        )

class CursoPensumModelForm(forms.ModelForm):
    class Meta:
        model = CursoPensum
        fields = (
            'ciclo',
            'curso',
            'creditos',
            'obligatorio',
            'curso_prerrequisito',
            'creditos_prerrequisito'
        )