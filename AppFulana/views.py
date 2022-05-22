from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PosteoForm, EditarForm, RegistrarseForm

# Create your views here.

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
            if user:
                login(request,user)
                return render (request, "AppFulana/inicio.html", {'mensaje':f"Hola {user}!"})
        else:
            return render (request, "AppFulana/iniciarSesion.html", {'form':form})
    else:
        form = AuthenticationForm()

    return render (request, "AppFulana/iniciarSesion.html", {'form':form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarseForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()
            return render (request,"AppFulana/inicio.html", {'mensaje':"Usuario creado"})
    else:
        form = RegistrarseForm()

    return render (request, 'AppFulana/registrarse.html', {'form':form})

def inicio(request):
    return render (request, "AppFulana/inicio.html")

def pruebastemplate(request):
    return render (request, "AppFulana/pruebastemplate.html")

def blog(request):
    return render (request, "AppFulana/blog.html")

def acercaDe(request):
    return render (request, "AppFulana/acercaDe.html")

class BlogVista (ListView):
    model = Posteo
    template_name = "AppFulana/blog.html"
    paginate_by = 6
    ordering = ['-fechaPosteo']

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

class AutoresPosteos (ListView):
    model = Posteo
    template_name = "AppFulana/autores.html"

class EditarPosteo (LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = EditarForm
    success_url = "/AppFulana/TodosMisPosteos/"

class EliminarPosteo (DeleteView):
    model = Posteo
    success_url = "/AppFulana/TodosMisPosteos/"

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

def contacto (request):
    return render (request, "AppFulana/contacto.html")