from django.urls import path
from .views import (EdificioView, EdificioCrearView, EdificioEditarView,
                    SalonesView, SalonesCrearView, SalonesEditarView,
                    SalonesClasificacionView, SalonesClasificacionCrearView, 
                    SalonesClasificacionEditarView)


app_name = 'edificios'

urlpatterns = [
    #Edificios
    path('', EdificioView.as_view(), name='edificio'),
    path('crear/', EdificioCrearView.as_view(), name='edificio_crear'),
    path('editar/', EdificioEditarView.as_view(), name='edificio_editar'),
    #Salones
    path('salones/', SalonesView.as_view(), name='salones'),
    path('salones/crear/', SalonesCrearView.as_view(),
         name='salones_crear'),
    path('salones/editar/', SalonesEditarView.as_view(),
         name='salones_editar'),
    #Clasificación de salones
    path('salones/clasificacion', SalonesClasificacionView.as_view(),
         name='clasificacionSalones'),
    path('salones/clasificacion/crear/',
         SalonesClasificacionCrearView.as_view(), name='salon_clasificacion_crear'),
    path('salones/clasificacion/editar/',
         SalonesClasificacionEditarView.as_view(), name='salon_clasificacion_editar'),
         
    ]

