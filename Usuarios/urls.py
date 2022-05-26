from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration/iniciarSesion', views.inicio_sesion, name='InicioSesion'),
    path('registration/cerrarSesion', LogoutView.as_view(template_name='Usuarios/registration/cerrarSesion.html'), name='CerrarSesion'),
    path('registration/registrarse', views.registrarse, name='Registrarse'),
]