from django.contrib import admin

from .models import Carrera, Curso, Pensum

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Pensum)