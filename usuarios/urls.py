from django.urls import path

from .views import EstudianteListView, EstudianteUpdateView, EstudianteDetailView, EstudianteCreateView

app_name = 'usuarios'

urlpatterns = [
    path('estudiantes', EstudianteListView.as_view(), name='estudiante-list'),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name='estudiante-detail'),
    path('estudiantes/<int:pk>/update/', EstudianteUpdateView.as_view(), name='estudiante-update'),
    path('estudiantes/create/', EstudianteCreateView.as_view(), name='estudiante-create'),
]
