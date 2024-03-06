from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio),
    path('estudiantes/', crear_estudiante),
    path('curso/', crear_curso),
    path('profesor/', crear_profesor),
    path('ver_estudiantes/', ver_estudiantes),
]