from django import forms
from .models import Estudiante


class EstudianteCreateModelForm(forms.ModelForm):
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


class EstudianteUpdateModelForm(forms.ModelForm):
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