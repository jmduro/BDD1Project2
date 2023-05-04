from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    pass


class DocumentoIdentificacion(models.Model):
    nombre = models.CharField(max_length=30)


class Pais(models.Model):
    nombre = models.CharField(max_length=50)


class CertificacionNacimiento(models.Model):
    libro = models.CharField(max_length=5)
    acta = models.CharField(max_length=5)
    folio = models.CharField(max_length=5)


class Estudiante(models.Model):
    usuario = models.OneToOneField(
        'Usuario', on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(
        'DocumentoIdentificacion', on_delete=models.SET_NULL, null=True)
    num_identificacion = models.CharField(max_length=30, null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    carnet = models.CharField(max_length=15)
    pais = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True)
    telefono = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    certificacion_nacimiento = models.OneToOneField(
        'CertificacionNacimiento', on_delete=models.SET_NULL, null=True)
    habilitado = models.BooleanField(default=True)
