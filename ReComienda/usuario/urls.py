from django.urls import path
from . import views

urlpatterns = [
    path("bienvenido", views.bienvenido, name="bienvenido"),
    path("nuevo_usuario", views.nuevo_usuario, name="nuevo_usuario"),
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion", views.cerrar_sesion, name="cerrar_sesion"),	
    path("perfil/<int:id>", views.ver_perfil, name="ver_perfil")
    

   
]

