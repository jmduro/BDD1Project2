from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UsuarioAutenticable(AbstractUser):
    rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True)


class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    administrar_carreras = models.BooleanField(default=True)
    administrar_cursos = models.BooleanField(default=True)
    administrar_estudiantes = models.BooleanField(default=True)
    administrar_docentes = models.BooleanField(default=True)
    administrar_usuarios = models.BooleanField(default=True)
    validar_cargas_academicas = models.BooleanField(default=True)
    administrar_roles_y_permisos = models.BooleanField(default=True)
    administracion_de_edificios_y_salones = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
