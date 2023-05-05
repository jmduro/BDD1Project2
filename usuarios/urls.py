from django.urls import path

from .views import (EstudianteListaView, EstudianteCrearView,
                    EstudianteEditarView, DocenteListaView,
                    DocenteCrearView, DocenteEditarView,
                    UsuarioListaView, UsuarioCrearView,
                    UsuarioEditarView)

app_name = 'usuarios'

urlpatterns = [
    # Estudiantes
    path('estudiantes', EstudianteListaView.as_view(), name='lista-estudiante'),
    path('estudiantes/crear/', EstudianteCrearView.as_view(),
         name='crear-estudiante'),
    path('estudiantes/<int:pk>/editar/',
         EstudianteEditarView.as_view(), name='editar-estudiante'),
    # Docentes
    path('docentes', DocenteListaView.as_view(), name='lista-docente'),
    path('docentes/crear/', DocenteCrearView.as_view(), name='crear-docente'),
    path('docentes/<int:pk>/editar/',
         DocenteEditarView.as_view(), name='editar-docente'),
    # Usuarios
    path('usuarios', UsuarioListaView.as_view(), name='lista-usuario'),
    path('usuarios/crear/', UsuarioCrearView.as_view(), name='crear-usuario'),
    path('usuarios/<int:pk>/editar/',
         UsuarioEditarView.as_view(), name='editar-usuario'),
]
