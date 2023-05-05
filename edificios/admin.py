from django.contrib import admin

from .models import Edificio, Salon, Salon_clasificacion

# Register your models here.

admin.site.register(Edificio)
admin.site.register(Salon)
admin.site.register(Salon_clasificacion)