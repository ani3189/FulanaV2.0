from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#formulario para registrarse

class RegistrarseForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {
            'username': None, #quitar el texto de ayuda para nombre de usuario
        }
    def __init__(self, *args, **kwargs):
        super(RegistrarseForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'        