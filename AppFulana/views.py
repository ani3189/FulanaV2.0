from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PosteoForm, EditarForm

# vista de inicio

def inicio(request):
    return render (request, "AppFulana/inicio.html") 
    
# vista de acerca de mi
     
def acercaDe(request):
    return render (request, "AppFulana/acercaDe.html")

# vista de la página blog donde se muestran los últimos 6 posteos y un slice del post

class BlogVista (ListView):
    model = Posteo
    template_name = "AppFulana/blog.html"
    ordering = ['-fechaPosteo']
    paginate_by = 6

# vista del posteo individual con botón eliminar y editar si corresponde al usuario

class PostIndividual (DetailView):
    model = Posteo
    template_name = "AppFulana/posteoIndividual.html"

# vista de los posteos del usuario logueado

class TodosMisPosteos (LoginRequiredMixin, ListView):
    model = Posteo
    template_name = "AppFulana/todosMisPosteos.html"
    def get_queryset(self):
        return Posteo.objects.filter(autorPosteo=self.request.user)

# vista para crear un nuevo posteo del usuario logueado

class NuevoPosteo (LoginRequiredMixin, CreateView, User):
    model = Posteo
    form_class = PosteoForm
    success_url = "/AppFulana/TodosMisPosteos/"

# vista de todos los posteos de todos los usuarios

class TodosLosPosteos (ListView):
    model = Posteo
    template_name = "AppFulana/todosLosPosteos.html"
    ordering = ['-fechaPosteo']

# vista para editar un posteo

class EditarPosteo (LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = EditarForm
    success_url = "/AppFulana/TodosMisPosteos/"

# vista para eliminar un posteo

class EliminarPosteo (DeleteView):
    model = Posteo
    success_url = "/AppFulana/TodosMisPosteos/"

# vista para buscar un posteo

def busquedaPosteo (request):
    return render (request, "AppFulana/todosLosPosteos.html")

def buscarPosteo (request):
    if request.GET['palabra']:
        palabra = request.GET ['palabra']
        posteos =  Posteo.objects.filter(bodyPosteo__icontains=palabra)
        return render (request, "AppFulana/buscarPosteo.html", {'palabra':palabra, 'posteos':posteos})
    else:
        respuesta = "No se encontraron posteos"
    return render (request, "AppFulana/buscarPosteo.html", {'respuesta':respuesta})

# vista para buscar un autor

def busquedaAutor (request):
    return render (request, "AppFulana/todosLosPosteos.html")

def buscarAutor (request):
    if request.GET['autor']:
        autor = request.GET ['autor']
        posteos =  Posteo.objects.filter(autorPosteo__username__icontains=autor)
        return render (request, "AppFulana/buscarAutor.html", {'autor':autor, 'posteos':posteos})
    else:
        respuesta = "No se encontraron posteos"
    return render (request, "AppFulana/buscarAutor.html", {'respuesta':respuesta})
