from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Profesor, Post 
from .forms import AlumnoForm, BuscarProfesorForm, ProfesorForm
from django.db.models import Q

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'PrimeraPagina/lista_alumnos.html', {'alumnos': alumnos,})

def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'PrimeraPagina/detalle_alumno.html', {'alumno': alumno})

def index(request): 
    posteos = Post.objects.all().order_by('-fecha_creacion')  # Ordenar por fecha de creación (más recientes primero)
    return render(request, 'PrimeraPagina/index.html', {'posteos': posteos})

def ingreso_alumnos(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            if request.user.is_authenticated:
                alumno.autor = request.user
                alumno.save()
                return redirect("PrimeraPagina:lista_alumnos")
        else:
            form.add_error(None, "El usuario debe estar logueado para subir una publicacion.")
    else:
        form = AlumnoForm()
    return render(request, 'PrimeraPagina/ingreso_alumnos.html', context={'form': form})

from django.shortcuts import render

def registro_profesores(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el profesor en la base de datos
            return redirect("PrimeraPagina:index")  # Redirige al inicio después de registrar
    else:
        form = ProfesorForm()
    return render(request, "PrimeraPagina/registro_profesores.html", {"form": form})

def publica_post(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        Post.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('PrimeraPagina:index')  # Redirige al index después de crear el post
    return render(request, 'PrimeraPagina/publica_post.html')

def buscar_profesores(request):
    profesores = None
    form = BuscarProfesorForm(request.GET)
    if request.method == 'GET' and 'termino' in request.GET: 
        form = BuscarProfesorForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            profesores = Profesor.objects.filter(
            Q(nombre__icontains=termino) |
            Q(apellido__icontains=termino) |
            Q(profesion__icontains=termino)
            )
    
    return render(request, 'PrimeraPagina/buscar_profesores.html', {'form': form, 'profesores': profesores})