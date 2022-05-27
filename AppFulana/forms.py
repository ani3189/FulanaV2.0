from dataclasses import field
from django import forms
from .models import Posteo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# formulario para crear nuevo posteo

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ('fechaPosteo','tituloPosteo', 'autorPosteo', 'bodyPosteo')
        widgets = {
            'fechaPosteo': forms.DateInput(attrs={'class':"wpcf7", 'placeholder':'AAAA-MM-DD'}),
            'tituloPosteo': forms.TextInput(attrs={'class':"wpcf7"}), 
            'autorPosteo': forms.TextInput(attrs={'class':"wpcf7", 'value':'', 'id':'usuarioPosteo', 'type':'hidden'}),
            #'autorPosteo': forms.Select(attrs={'class':"wpcf7"}), 
            'bodyPosteo': forms.Textarea(attrs={'class':"wpcf7"}),
        }

# formulario para editar posteo

class EditarForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ('fechaPosteo','tituloPosteo', 'bodyPosteo')
        widgets = {
            'fechaPosteo': forms.DateInput(attrs={'class':"wpcf7", 'placeholder':'AAAA-MM-DD'}),
            'tituloPosteo': forms.TextInput(attrs={'class':"wpcf7"}), 
            'bodyPosteo': forms.Textarea(attrs={'class':"wpcf7"}),
        }