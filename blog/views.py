

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm

# Autor CRUD
class AutorListView(ListView):
    model = Autor
    paginate_by = 20

class AutorDetailView(DetailView):
    model = Autor

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('blog:autor-list')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('blog:autor-list')

class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('blog:autor-list')

# Editora CRUD
class EditoraListView(ListView):
    model = Editora
    paginate_by = 20

class EditoraDetailView(DetailView):
    model = Editora

class EditoraCreateView(CreateView):
    model = Editora
    form_class = EditoraForm
    success_url = reverse_lazy('blog:editora-list')

class EditoraUpdateView(UpdateView):
    model = Editora
    form_class = EditoraForm
    success_url = reverse_lazy('blog:editora-list')

class EditoraDeleteView(DeleteView):
    model = Editora
    success_url = reverse_lazy('blog:editora-list')

# Livro CRUD
class LivroListView(ListView):
    model = Livro
    paginate_by = 20

class LivroDetailView(DetailView):
    model = Livro

class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('blog:livro-list')

class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('blog:livro-list')

class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('blog:livro-list')

# Publica CRUD
class PublicaListView(ListView):
    model = Publica
    paginate_by = 20

class PublicaDetailView(DetailView):
    model = Publica

class PublicaCreateView(CreateView):
    model = Publica
    form_class = PublicaForm
    success_url = reverse_lazy('blog:publica-list')

class PublicaUpdateView(UpdateView):
    model = Publica
    form_class = PublicaForm
    success_url = reverse_lazy('blog:publica-list')

class PublicaDeleteView(DeleteView):
    model = Publica
    success_url = reverse_lazy('blog:publica-list')