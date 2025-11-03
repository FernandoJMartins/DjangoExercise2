from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Autor
    path('autores/', views.AutorListView.as_view(), name='autor-list'),
    path('autores/add/', views.AutorCreateView.as_view(), name='autor-add'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),
    path('autores/<int:pk>/edit/', views.AutorUpdateView.as_view(), name='autor-edit'),
    path('autores/<int:pk>/delete/', views.AutorDeleteView.as_view(), name='autor-delete'),

    # Editora
    path('editoras/', views.EditoraListView.as_view(), name='editora-list'),
    path('editoras/add/', views.EditoraCreateView.as_view(), name='editora-add'),
    path('editoras/<int:pk>/', views.EditoraDetailView.as_view(), name='editora-detail'),
    path('editoras/<int:pk>/edit/', views.EditoraUpdateView.as_view(), name='editora-edit'),
    path('editoras/<int:pk>/delete/', views.EditoraDeleteView.as_view(), name='editora-delete'),

    # Livro
    path('livros/', views.LivroListView.as_view(), name='livro-list'),
    path('livros/add/', views.LivroCreateView.as_view(), name='livro-add'),
    path('livros/<int:pk>/', views.LivroDetailView.as_view(), name='livro-detail'),
    path('livros/<int:pk>/edit/', views.LivroUpdateView.as_view(), name='livro-edit'),
    path('livros/<int:pk>/delete/', views.LivroDeleteView.as_view(), name='livro-delete'),

    # Publica
    path('publicacoes/', views.PublicaListView.as_view(), name='publica-list'),
    path('publicacoes/add/', views.PublicaCreateView.as_view(), name='publica-add'),
    path('publicacoes/<int:pk>/', views.PublicaDetailView.as_view(), name='publica-detail'),
    path('publicacoes/<int:pk>/edit/', views.PublicaUpdateView.as_view(), name='publica-edit'),
    path('publicacoes/<int:pk>/delete/', views.PublicaDeleteView.as_view(), name='publica-delete'),
]
