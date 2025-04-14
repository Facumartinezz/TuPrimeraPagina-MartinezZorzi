from django.shortcuts import render, get_object_or_404
from .models import Alumno, Profesor, Curso, Entregable

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'PrimeraPagina/lista_alumnos.html', {'alumno': alumnos,})

def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'PrimeraPagina/detalle_alumno.html', {'estudiante': alumno})