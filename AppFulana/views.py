from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
    success_url = "/AppFulana/TodosMisPosteos/"
    fields = ['fechaPosteo','tituloPosteo', 'autorPosteo', 'bodyPosteo']

class TodosLosPosteos (ListView):
    model = Posteo
    template_name = "AppFulana/todosLosPosteos.html"

def busquedaPosteo (request):
    return render (request, "AppFulana/todosLosPosteos.html")

def buscarPosteo (request):
    if request.GET['palabra']:
        palabra = request.GET ['palabra']
        posteos =  Posteo.objects.filter(bodyPosteo__icontains=palabra)
        return render (request, "AppFulana/buscarPosteo.html", {'palabra':palabra, 'posteos':posteos})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)