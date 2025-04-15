from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Profesor, Post
from .forms import AlumnoForm

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
        # Aquí puedes manejar los datos enviados por el formulario
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        profesion = request.POST.get("profesion")
        contraseña = request.POST.get("contraseña")
        # Procesa los datos o guárdalos en la base de datos
        print(f"Profesor registrado: {nombre} {apellido}, {email}, {profesion}")
    return render(request, "PrimeraPagina/registro_profesores.html")

def crear_post(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        Post.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('PrimeraPagina:index')  # Redirige al index después de crear el post
    return render(request, 'PrimeraPagina/crear_post.html')