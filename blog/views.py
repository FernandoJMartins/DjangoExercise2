from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, "home.html", {})



