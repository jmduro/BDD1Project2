from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

Usuario = get_user_model()


class CustomCreationUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username',)
        field_classes = {'username': UsernameField}
