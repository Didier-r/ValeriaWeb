from email.policy import default
from random import choice
from django.db import models

# Create your models here.
class Project(models.Model):
    PLAN_CHOICES = [
    ('I', 'Individual'),
    ('A', 'Amigos'),
]
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(default='default@example.com')
    sedula = models.CharField(max_length=200, default='00000000')
    description = models.TextField(default='Sin descripción')
    plan = models.CharField(max_length=1, choices=PLAN_CHOICES, default='I')
    
   
        

    