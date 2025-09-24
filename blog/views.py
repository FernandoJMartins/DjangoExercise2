from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def ola(request):
    return HttpResponse("Você digitou olá")

def info(request):
    data =  {"disciplina:" : "RAD", "framework:" : "Django", "semestre:" : "2025.2s"}
    return JsonResponse(data)