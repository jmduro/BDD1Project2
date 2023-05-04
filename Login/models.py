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

