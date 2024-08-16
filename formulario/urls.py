
from django.urls import path
from . import views
urlpatterns = [
    path('',views.crear_usuario),
    path('hello/<str:usuario>',views.hello),
    path('projects',views.Projects)
]
