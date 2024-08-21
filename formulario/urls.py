
from django.urls import path
from . import views
urlpatterns = [
    path('formulario',views.crear_usuario,name="formulario"),
    path('',views.index,name='index'),
    path('projects',views.Projects)
]
