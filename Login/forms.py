from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class CustomeCreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",
                  'nombre',
                  'apellido',
                  'correo',
                  'telefono',
                  )
        field_classes = {'username': UsernameField}
