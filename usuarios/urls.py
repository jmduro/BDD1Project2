from django.urls import path

from .views import (EstudianteListView, EstudianteCreateView,
                    EstudianteUpdateView, DocenteListView,
                    DocenteCreateView, DocenteUpdateView,
                    UsuarioListView, UsuarioCreateView,
                    UsuarioUpdateView)

app_name = 'usuarios'

urlpatterns = [
    # Estudiantes
    path('estudiantes', EstudianteListView.as_view(), name='estudiante-list'),
    path('estudiantes/create/', EstudianteCreateView.as_view(),
         name='estudiante-create'),
    path('estudiantes/<int:pk>/update/',
         EstudianteUpdateView.as_view(), name='estudiante-update'),
    # Docentes
    path('docentes', DocenteListView.as_view(), name='docente-list'),
    path('docentes/create/', DocenteCreateView.as_view(), name='docente-create'),
    path('docentes/<int:pk>/update/',
         DocenteUpdateView.as_view(), name='docente-update'),
    # Usuarios
    path('usuarios', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/update/',
         UsuarioUpdateView.as_view(), name='usuario-update'),
]
