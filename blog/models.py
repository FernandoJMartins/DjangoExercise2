from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.ISBN})"


class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.autor} → {self.livro}"