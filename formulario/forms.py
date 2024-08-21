from django import forms
from .models import Project

class CrearNewUsuario(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-group form-control',  # Añade 'form-control' para los estilos
            'placeholder': 'Ingresa tu nombre'  # Ejemplo de placeholder opcional
        })
    )
    apellido = forms.CharField(
        label="Apellido",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-group form-control',
            'placeholder': 'Ingresa tu apellido'
        })
    )
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-group form-control'  # Añade la clase para el control de fecha
        })
    )
    correo = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-group form-control',
            'placeholder': 'Ingresa tu correo electrónico'
        })
    )
    sedula = forms.CharField(
        label="Cédula",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-group form-control',
            'placeholder': 'Ingresa tu cédula'
        })
    )
    description = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={
            'class': 'form-group form-control',
            'placeholder': 'Escribe una breve descripción'
        })
    )
    plan = forms.ChoiceField(
        label="Plan",
        choices=Project.PLAN_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-group form-control'  # Clase para select
        })
    )
