from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Profesor, Post, Avatar
from .forms import AlumnoForm, BuscarProfesorForm, ProfesorForm, EditarPerfilForm, AvatarForm
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            # Manejar el avatar
            avatar, created = Avatar.objects.get_or_create(user=user)
            if 'avatar' in request.FILES:
                avatar.imagen = request.FILES['avatar']
                avatar.save()
            return redirect('PrimeraPagina:index')  # Redirige al inicio después de guardar
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'PrimeraPagina/editar_perfil.html', {'form': form})

@login_required
def subir_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.avatar)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AvatarForm(instance=request.user.avatar)
    return render(request, 'subir_avatar.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'PrimeraPagina/lista_alumnos.html', {'alumnos': alumnos,})

def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'PrimeraPagina/detalle_alumno.html', {'alumno': alumno})

def index(request): 
    posteos = Post.objects.all().order_by('-fecha_creacion')  # Ordenar por fecha de creación (más recientes primero)
    return render(request, 'PrimeraPagina/index.html', {'posteos': posteos})

@login_required
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

@login_required
def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('PrimeraPagina:lista_alumnos')
    else:
        form = AlumnoForm(instance=estudiante)
    return render(request, 'PrimeraPagina/actualizar_estudiante.html', {'form': form})

def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)  # Obtiene el alumno por su ID o lanza un error 404 si no existe
    return render(request, 'PrimeraPagina/detalle_alumno.html', {'alumno': alumno})

@login_required
def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)  # Obtiene el alumno por su ID o lanza un error 404 si no existe
    if request.method == "POST":
        alumno.delete()  # Elimina el alumno de la base de datos
        return redirect('PrimeraPagina:lista_alumnos')  # Redirige a la lista de alumnos
    return render(request, 'PrimeraPagina/eliminar_alumno.html', {'alumno': alumno})

@login_required
def registro_profesores(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el profesor en la base de datos
            return redirect("PrimeraPagina:index")  # Redirige al inicio después de registrar
    else:
        form = ProfesorForm()
    return render(request, "PrimeraPagina/registro_profesores.html", {"form": form})

@login_required
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

def about(request):
    return render(request, 'PrimeraPagina/about.html')

def pages(request):
    # Aquí puedes cargar los blogs desde la base de datos
    blogs = Post.objects.all()
    return render(request, 'PrimeraPagina/pages.html', {'blogs': blogs})

def detalle_blog(request, pk):
    blog = get_object_or_404(Post, pk=pk)  # Obtiene el blog por su ID o lanza un error 404 si no existe
    return render(request, 'PrimeraPagina/detalle_blog.html', {'blog': blog})