from django.shortcuts import render
from AppCoder.models import Estudiantes, Curso, Profesor
from AppCoder.forms import EstudiantesForm, CursoForm, ProfesorForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudiantesForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Estudiantes(
                nombre = dic['nombre'],
                apellido = dic['apellido'],
                email = dic['email'],
                edad = dic['edad']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = EstudiantesForm()
    return render(request, 'crear_estudiantes.html', {'form': formulario})

def crear_curso(request):
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Curso(
                nombre = dic['nombre'],
                camada = dic['camada']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = CursoForm()
    return render(request, 'crear_cursos.html', {'form': formulario})

def crear_profesor(request):
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Profesor(
                nombre = dic['nombre'],
                apellido = dic['apellido'],
                email = dic['email'],
                profesion = dic['profesion']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = ProfesorForm()
    return render(request, 'crear_profesores.html', {'form': formulario})

def ver_estudiantes(request):
    if request.GET:
        if request.GET['nombre'] and request.GET['apellido']:
            nombre = request.GET['nombre']
            apellido = request.GET['apellido']
            estudiante = Estudiantes.objects.filter(nombre__icontains = nombre, apellido__icontains = apellido)
            mensaje = f"Estamos buscando al estudiante {nombre} {apellido}"
            return render(request, 'ver_estudiantes.html', {'mensaje': mensaje, 'resultados': estudiante})
        else:
            mensaje = "No se ha buscado nada"
            return render(request, 'ver_estudiantes.html', {'mensaje': mensaje})
    return render(request, 'ver_estudiantes.html')