from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo= models.EmailField()
    telefono= models.CharField(max_length=20)
    is_organisor=models.BooleanField(default=True)
    is_agent=models.BooleanField(default=False)


class Rol(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    administrar_carreras=models.BooleanField(default=True)
    administrar_cursos=models.BooleanField(default=True)
    administrar_estudiantes=models.BooleanField(default=True)
    administrar_docentes=models.BooleanField(default=True)
    administrar_usuarios=models.BooleanField(default=True)
    validar_cargas_academicas=models.BooleanField(default=True)
    administrar_roles_y_permisos=models.BooleanField(default=True)
    administracion_de_edificios_y_salones=models.BooleanField(default=True)
    habilitado=models.BooleanField(default=True)
   

    def __str__(self):
        return f"{self.nombre} {self.descripcion} {self.habilitado}"



