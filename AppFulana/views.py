from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, loader
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PosteoForm, EditarForm
from django.urls import reverse

# Create your views here.

def inicio(request):
    return render (request, "AppFulana/inicio.html")
    
def acercaDe(request):
    return render (request, "AppFulana/acercaDe.html")

class BlogVista (ListView):
    model = Posteo
    template_name = "AppFulana/blog.html"
    ordering = ['-fechaPosteo']
    paginate_by = 6

class PostIndividual (DetailView):
    model = Posteo
    template_name = "AppFulana/posteoIndividual.html"

class TodosMisPosteos (LoginRequiredMixin, ListView):
    model = Posteo
    template_name = "AppFulana/todosMisPosteos.html"
    def get_queryset(self):
        return Posteo.objects.filter(autorPosteo=self.request.user)

class NuevoPosteo (LoginRequiredMixin, CreateView, User):
    model = Posteo
    form_class = PosteoForm
    success_url = "/AppFulana/TodosMisPosteos/"

class TodosLosPosteos (ListView):
    model = Posteo
    template_name = "AppFulana/todosLosPosteos.html"
    ordering = ['-fechaPosteo']


class EditarPosteo (LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = EditarForm
    success_url = "/AppFulana/TodosMisPosteos/"

class EliminarPosteo (DeleteView):
    model = Posteo
    success_url = "/AppFulana/TodosMisPosteos/"

# habilitar cuando sepa como pasar el args con un path con (r'^(?P<pk>\d+)$')
# def like (request, pk):
#     posteo = get_object_or_404(Posteo, id=request.POST.get('posteo_id'))
#     posteo.likes.add(request.user)
#     return HttpResponseRedirect(reverse(PostIndividual, args=(r'^(?P<pk>\d+)$')))

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
