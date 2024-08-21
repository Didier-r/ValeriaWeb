from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project
from django.shortcuts import get_list_or_404,render,redirect
from .forms import CrearNewUsuario
# Create your views here.

    
def index(request):
    return render(request,'index.html')

def Quienes_Somos(request):
    return render(request,'quienesSomos.html')

def crear_usuario(request):
    if request.method == 'GET':
        return render(request,'formulario.html',{
        'form': CrearNewUsuario()
    })
    else:
        Project.objects.create(nombre=request.POST['nombre'],apellido=request.POST['apellido'],fecha_nacimiento=request.POST['fecha_nacimiento'],correo=request.POST['correo'],sedula=request.POST['sedula'],description=request.POST['description'],plan=request.POST['plan'])
        return redirect('index')
    
def planes_Entrenamiento(request):
    return render(request,'planesEntrenamiento.html')

def clases_grupales(request):
    return render(request,'ClasesGrupales.html')
    
    
    