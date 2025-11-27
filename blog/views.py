from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Livro
from .forms import LivroForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, "home.html", {})



def livro_list(request):
    livros_list = Livro.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(livros_list, 10)  
    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.page(1)
    except EmptyPage:
        livros = paginator.page(paginator.num_pages)

    return render(request, 'livro_list.html', {'livros': livros})


def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:livro-list')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form': form, 'action': 'Criar'})


def livro_edit(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('blog:livro-list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form': form, 'action': 'Editar'})
