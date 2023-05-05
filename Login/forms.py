from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Rol

Usuario = get_user_model()


class CustomCreationUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username',)
        field_classes = {'username': UsernameField}


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = (
            'nombre',
            'descripcion',
        )


class RolForm2(forms.ModelForm):
    class Meta:
        model = Rol
        fields = (
            'nombre',
            'descripcion',
            'habilitado'
        )


class RolForm3(forms.ModelForm):
    class Meta:
        model = Rol
        fields = (
            'administrar_carreras',
            'administrar_cursos',
            'administrar_estudiantes',
            'administrar_docentes',
            'administrar_usuarios',
            'validar_cargas_academicas',
            'administrar_roles_y_permisos',
            'administracion_de_edificios_y_salones'
        )
