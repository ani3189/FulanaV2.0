from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .forms import RegistrarseForm
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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
            return render (request, "registration/iniciarSesion.html", {'form':form})
    else:
        form = AuthenticationForm()

    return render (request, "registration/iniciarSesion.html", {'form':form})

# Opción de registro V2
class Registrarse(generic.CreateView):
    form_class = RegistrarseForm
    template_name = 'registration/registrarse.html'
    success_url = reverse_lazy('InicioSesion')

@login_required
def editar_usuario (request): # --->  cambiar a UserChangeForm para ver si funciona
    usuario = request.user
    if request.method == "POST":
        miFormulario = RegistrarseForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data 
            usuario.username = informacion['username']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']

            usuario.save()
            
            return render (request, "AppFulana/inicio.html")
    else:
        miFormulario=RegistrarseForm(initial={
            'username':usuario.username, 
            'first_name':usuario.first_name,
            'last_name':usuario.last_name, 
            'email':usuario.email})

    return render (request, "registration/editarPerfil.html",{'miFormulario':miFormulario, 'usuario':usuario.username, 'email':usuario.email})

# Opción de registro V1

# def registrarse(request):
#     if request.method == 'POST':
#         form = RegistrarseForm(request.POST)
#         if form.is_valid():
#             user=form.cleaned_data['username']
#             form.save()
#             return render (request,"AppFulana/inicio.html", {'mensaje':"Usuario creado"})
#     else:
#         form = RegistrarseForm()

#     return render (request, 'registration/registrarse.html', {'form':form})

