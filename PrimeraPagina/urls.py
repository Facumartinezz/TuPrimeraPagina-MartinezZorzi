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

app_name = 'PrimeraPagina'
urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path("alumnos/create", views.ingreso_alumnos, name="ingreso_alumnos"),
    path('profesores/create', views.registro_profesores, name='registro_profesores'),
    path('post/create', views.publica_post, name='publica_post'),
    path('profesores/buscar', views.buscar_profesores, name='buscar_profesores'),
    
]