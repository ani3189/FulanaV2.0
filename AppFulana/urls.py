from django.urls import path
from AppFulana import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('pruebastemplate', views.pruebastemplate, name="PruebasTemplate"),
    path('blog', views.BlogVista.as_view(), name="Blog"),
    path('acercaDe', views.acercaDe, name="AcercaDe"),
    path(r'^(?P<pk>\d+)$', views.PostIndividual.as_view(), name='PostIndividual'),
    path('inicioSesion', views.inicio_sesion, name='InicioSesion'),
    path('cerrarSesion', LogoutView.as_view(template_name='AppFulana/cerrarSesion.html'), name='CerrarSesion'),
    path('TodosMisPosteos', views.TodosMisPosteos.as_view(), name='TodosMisPosteos'),
    path('TodosLosPosteos/', views.TodosLosPosteos.as_view(), name='TodosLosPosteos'),
    path('buscarPosteo/', views.buscarPosteo),
]