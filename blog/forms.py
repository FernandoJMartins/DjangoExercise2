from django import forms
from .models import Livro

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
