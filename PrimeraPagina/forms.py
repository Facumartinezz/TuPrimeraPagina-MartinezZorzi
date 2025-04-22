from django import forms
from .models import Alumno, Profesor, Avatar
from django.contrib.auth.forms import User

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'email']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'contraseña', 'profesion']

class BuscarProfesorForm(forms.Form):
    termino = forms.CharField(
        max_length=100, label="Buscar Profesor", 
        widget=forms.TextInput(attrs={'class': 'form-control', 
        'placeholder': 'Nombre o Apellido'})
        )
from django import forms
from django.contrib.auth.models import User

class EditarPerfilForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, label="Cambiar Avatar")  # Campo para el avatar

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Campos editables
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']