from django.contrib import admin

from .models import Carrera, Curso, Pensum, Ciclo, CursoPensum

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Pensum)
admin.site.register(Ciclo)
admin.site.register(CursoPensum)