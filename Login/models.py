from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UsuarioAutenticable(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, null=True)
    correo= models.EmailField()
    telefono= models.CharField(max_length=20)
    is_organisor=models.BooleanField(default=True)
    is_agent=models.BooleanField(default=False)
    rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True)


class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    administrar_carreras = models.BooleanField(default=False)
    administrar_cursos = models.BooleanField(default=False)
    administrar_estudiantes = models.BooleanField(default=False)
    administrar_docentes = models.BooleanField(default=False)
    administrar_usuarios = models.BooleanField(default=False)
    validar_cargas_academicas = models.BooleanField(default=False)
    administrar_roles_y_permisos = models.BooleanField(default=False)
    administracion_de_edificios_y_salones = models.BooleanField(default=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
