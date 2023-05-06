from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from .models import Rol
from usuarios.models import Estudiante, Docente, Usuario

class LoginRequeridoMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


# --------------------------------------------------------------------
# PENSUM


class AdministrarCarrerasMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        rol = request.user.rol
        if not rol.administrar_carreras:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


class AdministrarCursosMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.rol.administrar_cursos:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


# --------------------------------------------------------------------
# USUARIOS


class AdministrarEstudiantesMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        rol = request.user.rol
        if not rol.administrar_estudiantes:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


class AdministrarDocentesMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.rol.administrar_docentes:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


class AdministrarUsuariosMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        rol = request.user.rol
        if not rol.administrar_usuarios:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


# --------------------------------------------------------------------
# CARGAS


class ValidarCargasAcademicasMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.rol.validar_cargas_academicas:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


# --------------------------------------------------------------------
# SEGURIDAD


class AdministrarRolesPermisosMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.rol.administrar_roles_y_permisos:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)


# --------------------------------------------------------------------
# EDIFICIOS


class AdministrarEdificiosSalonesMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.rol.administracion_de_edificios_y_salones:
            return redirect('inicio/')
        return super().dispatch(request, *args, **kwargs)
