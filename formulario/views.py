from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project
from django.shortcuts import get_list_or_404,render
from .forms import CrearNewUsuario
# Create your views here.

    
def hello(request,usuario):
    print(usuario)
    return HttpResponse("<h1>Hello World</h1>")

def Projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)
def crear_usuario(request):
    print(request.GET['nombre'])
    print(request.GET['apellido'])
    print(request.GET['fecha_nacimiento'])
    print(request.GET['correo'])
    print(request.GET['sedula'])
    print(request.GET['description'])
    print(request.GET['plan'])
    Project.objects.create(nombre=request.GET['nombre'],apellido=request.GET['apellido'],fecha_nacimiento=request.GET['fecha_nacimiento'],correo=request.GET['correo'],sedula=request.GET['sedula'],description=request.GET['description'],plan=request.GET['plan'])
    return render(request,'formulario.html',{
        'form': CrearNewUsuario()
    })