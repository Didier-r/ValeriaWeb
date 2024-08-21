
from django.urls import path
from . import views
urlpatterns = [
    path('formulario',views.crear_usuario,name="formulario"),
    path('',views.index,name='index'),
    path('quienesSomos',views.Quienes_Somos,name='quienesSomos'),
    path('planesEntrenamiento',views.planes_Entrenamiento,name='planesEntrenamiento'),
    path('clases_grupales',views.clases_grupales,name='clases_grupales')
    
]
