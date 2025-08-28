from django.urls import path
from . import views

urlpatterns = [
    path("estudiantes/", views.lista_estudiantes, name="lista_estudiantes"),
    path("estudiantes/nuevo/", views.crear_estudiante, name="crear_estudiante"),
    path("estudiantes/<int:pk>/editar/", views.editar_estudiante, name="editar_estudiante"),
    path("estudiantes/<int:pk>/eliminar/", views.eliminar_estudiante, name="eliminar_estudiante"),
]
