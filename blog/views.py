from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, "home.html", {})



def livro_list(request):
    from .models import Livro
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    livros_list = Livro.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(livros_list, 2)  
    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.page(1)
    except EmptyPage:
        livros = paginator.page(paginator.num_pages)

    return render(request, 'livro_list.html', {'livros': livros})
