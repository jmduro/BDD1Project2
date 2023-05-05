from django.urls import path
from .views import carrera, crear_carrera, pensum, curso, editar_carrera, crear_curso, editar_curso
from .views import crear_pensum, editar_pensum, ciclo, crear_ciclo, curso_pensum, agregar_curso, editar_curso_pensum

app_name = "pensum"

urlpatterns = [
    path('carrera/', carrera, name='carrera'),
    path('crear_carrera/', crear_carrera, name='crear_carrera'),
    path('editar_carrera/<pk>', editar_carrera, name='editar_carrera'),
    path('crear_pensum/', crear_pensum, name='crear_pensum'),
    path('pensum/<pk>', pensum, name='pensum'),
    path('editar_pensum/<pk>', editar_pensum, name='editar_pensum'),
    path('curso/', curso, name='curso'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('editar_curso/<pk>', editar_curso, name='editar_curso'),
    path('ciclo/<pk>', ciclo, name='ciclo'),
    path('crear_ciclo/', crear_ciclo, name='crear_ciclo'),
    path('curso_pensum/<pk>', curso_pensum, name='curso_pensum'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
    path('editar_curso_pensum/<pk>', editar_curso_pensum, name='editar_curso_pensum'),
]