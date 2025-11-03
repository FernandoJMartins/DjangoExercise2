from django import forms
from .models import Autor, Editora, Livro, Publica

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['ISBN', 'titulo', 'preco', 'estoque', 'editora']

class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        fields = ['livro', 'autor']