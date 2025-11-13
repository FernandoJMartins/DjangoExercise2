from django.core.management.base import BaseCommand
from blog.models import Livro, Editora
from faker import Faker
from decimal import Decimal

class Command(BaseCommand):
    help = 'Comando para criar livros'
    def handle(self, *args, **options):
        faker = Faker()
        cache_editora = {}
        for i in range(100):
            
            titulo = faker.sentence(nb_words=4)
            preco = Decimal(faker.pydecimal(left_digits=3, right_digits=2, positive=True))
            estoque = faker.random_int(min=0, max=50)
            isbn = faker.isbn13()
            editora_nome = faker.company()

            
            #reutiliza instâncias já criadas para evitar queries repetidas
            editora = cache_editora.get(editora_nome)
            if not editora:
                editora, _ = Editora.objects.get_or_create(nome=editora_nome)
                cache_editora[editora_nome] = editora

            Livro.objects.create(
                titulo=titulo,
                preco=preco,
                estoque=estoque,
                ISBN=isbn,
                editora=editora,
            )

        # A lógica do seu comando vai aqui
        self.stdout.write("Livros criados com sucesso!")
