"""
URL configuration for PrimeraPagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'PrimeraPagina'
urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path("alumnos/create", views.ingreso_alumnos, name="ingreso_alumnos"),
    path('alumnos/<int:pk>/update', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('alumnos/<int:pk>/', views.detalle_alumno, name='detalle_alumno'),  
    path('alumnos/<int:pk>/delete', views.eliminar_alumno, name='eliminar_alumno'), 
    path('profesores/create', views.registro_profesores, name='registro_profesores'),
    path('post/create', views.publica_post, name='publica_post'),
    path('profesores/buscar', views.buscar_profesores, name='buscar_profesores'),
    path('editarPerfil/', views.editar_perfil, name='editar_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='PrimeraPagina/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('subir_avatar/', views.subir_avatar, name='subir_avatar'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),  # Ruta para la vista de blogs
    path('pages/<int:pk>/', views.detalle_blog, name='detalle_blog'),  # Ruta para el detalle del blog


]
if settings.DEBUG: # hacemos esta validación para que servir los estaticos desde django solo en desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)