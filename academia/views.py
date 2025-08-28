from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from .forms import EstudianteForm
from .forms import MatriculaForm


# definimos un inicio para poder acceder a los url

def inicio(request):
    return render(request, 'inicio.html')





def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "academia/estudiante_lista.html", {"estudiantes": estudiantes})

def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_estudiantes")
    else:
        form = EstudianteForm()
    return render(request, "academia/estudiante_form.html", {"form": form})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect("lista_estudiantes")
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, "academia/estudiante_form.html", {"form": form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect("lista_estudiantes")



def crear_matricula(request):
    if request.method == "POST":
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_matriculas')
        
    else: 
        form = MatriculaForm()
    
    return render(request,'crear_matricula.html',{'form':form})