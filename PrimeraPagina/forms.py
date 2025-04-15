from django import forms
from .models import Alumno, Profesor

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