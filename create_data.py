import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webstore.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from produto.models import Produto

class Utils:
    """Metodos genericos"""
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))

class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random()* randint(10, 50),
                estoque=randint(10, 200)
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)

produtos = (
    'Himel',
    'Lápis de Olho',
    'Alicate de Unha',
    'Alicate de Cuticula',
    'Algodão 500 gr',
    'Algodão 250 gr',
    'Hidratante pele seca',
    'Hidratante pele ultra seca',
    'Sabonete Esfoliante',
    'Creme para as mãos',
    'Creme para os pés',
    'Lixa de unha',
    'Lixa para os pés',
    'Desodorante rolon 150 gr',
    'Esmalte vermelho',
    'Esmalte bege',
    'Esmalte roxo',
    'Tesoura',
    'Pinça Grande',
    'Pinça Media',
    'Pinça pquena',
)

tic = timeit.default_timer()
ProdutoClass.criar_produtos(produtos)
toc = timeit.default_timer()

print("Tempo", toc, tic )