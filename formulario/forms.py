from django import forms
from .models import Project
class CrearNewUsuario(forms.Form):
    nombre = forms.CharField(label="nombre",max_length=200)
    apellido = forms.CharField(label="apellido",max_length=200)   
    fecha_nacimiento = forms.DateField(label="fecha de nacieminto",widget=forms.DateInput(attrs={'type': 'date'}))
    correo = forms.EmailField(label="correo electronico",)
    sedula = forms.CharField(label="cedula",max_length=200)
    description = forms.CharField(label="descripcion",widget=forms.Textarea)
    plan = forms.ChoiceField(label="Plan", choices=Project.PLAN_CHOICES)
    