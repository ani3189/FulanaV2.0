from dataclasses import field
from django import forms
from .models import Posteo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ('fechaPosteo','tituloPosteo', 'autorPosteo', 'bodyPosteo')
        widgets = {
            'fechaPosteo': forms.DateInput(attrs={'class':"wpcf7", 'placeholder':'AAAA-MM-DD'}),
            'tituloPosteo': forms.TextInput(attrs={'class':"wpcf7"}), 
            'autorPosteo': forms.Select(attrs={'class':"wpcf7"}), 
            'bodyPosteo': forms.Textarea(attrs={'class':"wpcf7"}),
        }

class EditarForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ('fechaPosteo','tituloPosteo', 'bodyPosteo')
        widgets = {
            'fechaPosteo': forms.DateInput(attrs={'class':"wpcf7", 'placeholder':'AAAA-MM-DD'}),
            'tituloPosteo': forms.TextInput(attrs={'class':"wpcf7"}), 
            'bodyPosteo': forms.Textarea(attrs={'class':"wpcf7"}),
        }

class RegistrarseForm(UserCreationForm):
    username = forms.CharField()
    mail = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'mail', 'password1', 'password2']
