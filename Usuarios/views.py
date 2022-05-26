from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrarseForm
from django.contrib.auth import login, authenticate

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

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarseForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()
            return render (request,"AppFulana/inicio.html", {'mensaje':"Usuario creado"})
    else:
        form = RegistrarseForm()

    return render (request, 'registration/registrarse.html', {'form':form})
