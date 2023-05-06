from django import forms
from .models import Estudiante, Docente, Usuario


class EstudianteCrearModelForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = (
            # 'tipo_documento',
            'num_identificacion',
            'nombres',
            'apellidos',
            'carnet',
            # 'pais',
            'telefono',
            'fecha_nacimiento',
            'correo_electronico',
            # 'certificacion_nacimiento',
        )
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'autocomplete': 'off'}),
        }


class EstudianteEditarModelForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = (
            # 'tipo_documento',
            'num_identificacion',
            'nombres',
            'apellidos',
            'carnet',
            # 'pais',
            'telefono',
            'fecha_nacimiento',
            'correo_electronico',
            # 'certificacion_nacimiento',
            'habilitado'
        )
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'autocomplete': 'off'}),
        }


class DocenteCrearModelForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = (
            'nombres',
            'apellidos',
            'profesion',
            'acronimo',
            'correo_electronico',
            'cui',
            'telefono',
            'num_personal',
            # 'docente_titular',
        )


class DocenteEditarModelForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = (
            'nombres',
            'apellidos',
            'profesion',
            'acronimo',
            'correo_electronico',
            'cui',
            'telefono',
            'num_personal',
            # 'docente_titular',
            'habilitado'
        )


class UsuarioCrearModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'nombres',
            'apellidos',
            'profesion',
            'acronimo',
            'correo_electronico',
            'cui',
            'telefono',
            'num_personal',
        )


class UsuarioEditarModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'nombres',
            'apellidos',
            'profesion',
            'acronimo',
            'correo_electronico',
            'cui',
            'telefono',
            'num_personal',
            'habilitado'
        )
