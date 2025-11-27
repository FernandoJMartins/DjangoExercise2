from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Livro
from .forms import LivroForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth import *
from django.contrib.auth.decorators import *

@login_required(login_url='blog:signin')
def home(request):
    return render(request, "home.html", {})


@login_required(login_url='blog:signin')
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

@login_required(login_url='blog:signin')
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:livro-list')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form': form, 'action': 'Criar'})

@login_required(login_url='blog:signin')
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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:home')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('blog:home')