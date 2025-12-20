# ...existing code...
from django.urls import include, path
from . import views

app_name = "blog"

urlpatterns = [

    #API
    path('api/', include('blog.api_urls')),

    path('', views.home, name='home'),
    path('livros/', views.livro_list, name='livro-list'),
    path('livros/novo/', views.livro_create, name='livro-create'),
    path('livros/<int:pk>/editar/', views.livro_edit, name='livro-edit'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro-delete'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
# ...existing code...