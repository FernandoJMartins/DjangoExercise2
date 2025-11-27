from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Autor(models.Model):
    nome = models.CharField(max_length=150, unique=True)

class Editora(models.Model):
    nome = models.CharField(max_length=150, unique=True)

class Livro(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False)