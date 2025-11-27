from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'preco', 'estoque', 'ISBN', 'editora']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-control'}),
        }


class SignInForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model() # Added to fix reference

        fields = ['username', 'email', 'password1', 'password2']
    
    def cleanEmail(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email


