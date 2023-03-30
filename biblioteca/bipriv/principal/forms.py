from django import forms
from .models import Contas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input_reg', 'placeholder': 'Nome'}),
            'password1': forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Password'}),
         }
        labels = {
            'username': 'Queira ter a gentileza de nos dizer o seu nome',
            'password1': 'senha',

        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('Nome', 'Apelido', 'Telefone')
