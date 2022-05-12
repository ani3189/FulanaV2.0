from dataclasses import field
from django import forms
from .models import Posteo

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