# ...existing code...
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/', views.livro_list, name='livro-list'),
    path('livros/novo/', views.livro_create, name='livro-create'),
    path('livros/<int:pk>/editar/', views.livro_edit, name='livro-edit'),
]
# ...existing code...