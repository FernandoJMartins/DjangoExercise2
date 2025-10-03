from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

def home(request):

    produtos = [
        {"nome": "Notebook", "preco": 2500.00},
        {"nome": "Mouse", "preco": 85.50},
        {"nome": "Teclado", "preco": 24.00},
        {"nome": "Monitor", "preco": 150.90},
    ]
    
    contexto = {
        "usuario": "Fernando",         
        "numero": 5,                   
        "now": datetime.now(),          
        "is_logged_in": True,  
        "idade": 19,
        "admin": True,
        "role": "admin",  # Valores possíveis: 'admin' ou 'user'
        "produtos": produtos,  # Lista de produtos para exibir na tabela
                 
    }
    return render(request, "home.html", contexto)





def contato(request, phone):
    return render(request, "contato.html", {"telefone": phone})

def about(request):
    return render(request, "about.html", {})
