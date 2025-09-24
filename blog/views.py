from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def eco(request, texto):
    return HttpResponse(f'Você digitou {texto}')

def info(request):
    data =  {"disciplina:" : "RAD", "framework:" : "Django", "semestre:" : "2025.2s"}
    return JsonResponse(data)

def index(request):
    return HttpResponse("Bem-vindo ao meu Blog")