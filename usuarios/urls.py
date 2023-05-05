from django.urls import path

from .views import (EstudianteListView, EstudianteDetailView,
                    EstudianteCreateView, DocenteListView,
                    DocenteDetailView, DocenteCreateView)

app_name = 'usuarios'

urlpatterns = [
    # Estudiantes
    path('estudiantes', EstudianteListView.as_view(), name='estudiante-list'),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(),
         name='estudiante-detail'),
    path('estudiantes/create/', EstudianteCreateView.as_view(),
         name='estudiante-create'),
    # Docentes
    path('docentes', DocenteListView.as_view(), name='docente-list'),
    path('docentes/<int:pk>/', DocenteDetailView.as_view(), name='docente-detail'),
    path('docentes/create/', DocenteCreateView.as_view(), name='docente-create'),
]
