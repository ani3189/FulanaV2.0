from django.urls import path
from AppFulana import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('blog', views.BlogVista.as_view(), name="Blog"),
    path('acercaDe', views.acercaDe, name="AcercaDe"),
    path(r'^(?P<pk>\d+)$', views.PostIndividual.as_view(), name='PostIndividual'),
    path('TodosMisPosteos/', views.TodosMisPosteos.as_view(), name='TodosMisPosteos'),
    path('TodosLosPosteos/', views.TodosLosPosteos.as_view(), name='TodosLosPosteos'),
    path('buscarPosteo/', views.buscarPosteo, name='buscarPosteo'),
    path(r'^nuevo$', views.NuevoPosteo.as_view(), name='NuevoPosteo'),
    path(r'^editar/(?P<pk>\d+)$', views.EditarPosteo.as_view(), name='Editar'),
    path(r'^eliminar/(?P<pk>\d+)$', views.EliminarPosteo.as_view(), name='Eliminar'),
    path('buscarAutor/', views.buscarAutor, name='buscarAutor'),
    #path('like/<int:pk>', views.like, name='like_posteo'),
]