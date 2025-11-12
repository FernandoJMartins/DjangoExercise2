# ...existing code...
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/', views.livro_list, name='livro-list'),
]
# ...existing code...