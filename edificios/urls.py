from django.urls import path
from .views import (EdificioPage, EdificioCrearPage, EdificioEditarPage,
                    EdificioSalonesPage, EdificioSalonesCrearPage, EdificioSalonesEditarPage,
                    EdificioSalonesClasificacionPage, EdificioSalonesClasificacionCrearPage, 
                    EdificioSalonesClasificacionEditarPage, EdificioView)


app_name = 'edificios'

urlpatterns = [
    #Edificios
    path('', EdificioPage, name='edificio_page'),
    path('crear/', EdificioCrearPage, name='edificio_crear'),
    path('editar/', EdificioEditarPage, name='edificio_editar'),
    #Salones
    path('salones/', EdificioSalonesPage, name='edificio_salones'),
    path('salones/crear/', EdificioSalonesCrearPage,
         name='edificio_salones_crear'),
    path('salones/editar/', EdificioSalonesEditarPage,
         name='edificio_salones_editar'),
    #Clasificación de salones
    path('salones/clasificacion', EdificioSalonesClasificacionPage,
         name='edificio_clasificacionSalones'),
    path('salones/clasificacion/crear/',
         EdificioSalonesClasificacionCrearPage, name='salon_clasificacion_crear'),
    path('salones/clasificacion/editar/',
         EdificioSalonesClasificacionEditarPage, name='salon_clasificacion_editar'),
    ]

