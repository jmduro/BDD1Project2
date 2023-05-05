from django.contrib import admin
from django.urls import path, include
from Login import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from Login.views import SignupView, RolCreate, RolUpdate, RolModificar
from edificios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('roles/<int:pk>/editar/',RolUpdate),
    path('roles/<int:pk>/modificar/',RolModificar),
    path('', LoginView.as_view(), name='login'),
    path('roles/',views.RolPage,name='roles'),
    path('create-rol/',views.RolCreate,name='create_rol'),
    path('inicio/', views.HomePage, name='inicio'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('edificio/', EdificioPage, name='edificio_page'),
    path('edificio/crear/', EdificioCrearPage, name='edificio_crear'),
    path('edificio/editar/', EdificioEditarPage, name='edificio_editar'),
    path('edificio/salones/', EdificioSalonesPage, name='edificio_salones'),
    path('edificio/salones/crear/', EdificioSalonesCrearPage, name='edificio_salones_crear'),
    path('edificio/salones/editar/', EdificioSalonesEditarPage, name='edificio_salones_editar'),
    path('edificio/salones/clasificacion', EdificioSalonesClasificacionPage, name='edificio_clasificacionSalones'),
    path('edificio/salones/clasificacion/crear/', EdificioSalonesClasificacionCrearPage, name='salon_clasificacion_crear'),
    path('edificio/salones/clasificacion/editar/', EdificioSalonesClasificacionEditarPage, name='salon_clasificacion_editar'),


]
