from django.urls import path

from .views import EstudianteListView, EstudianteUpdateView, EstudianteDetailView, EstudianteCreateView, EstudianteDeleteView

app_name = 'usuarios'

urlpatterns = [
    path('', EstudianteListView.as_view(), name='estudiantes-list'),
    path('<int:pk>/', EstudianteDetailView.as_view(), name='estudiante-detail'),
    path('<int:pk>/update/', EstudianteUpdateView.as_view(), name='estudiante-update'),
    path('<int:pk>/delete/', EstudianteDeleteView.as_view(), name='estudiante-delete'),
    path('create/', EstudianteCreateView.as_view(), name='estudiante-create'),
]
