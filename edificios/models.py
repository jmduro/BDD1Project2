from django.db import models

# Create your models here.

class Edificio(models.Model):
    nombre = models.CharField(max_length=20)
    salones = models.IntegerField(default=0, null=False)
    niveles = models.IntegerField(default=0, null=False)
    fecha_creacion = models.DateField(auto_now=True, null=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

class Salon_clasificacion(models.Model):
    nombre = models.CharField(max_length=20)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

class Salon(models.Model):
    nombre = models.CharField(max_length=20)
    edificio = models.ForeignKey("Edificio", on_delete=models.SET_DEFAULT,null=True, default="")
    capacidad = models.IntegerField(default=0,null=False)
    salon_clasificacion = models.ForeignKey("Salon_clasificacion", on_delete=models.SET_DEFAULT,null=True, default="")
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

