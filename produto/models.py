from django.db import models
from django.urls.base import reverse_lazy

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque minimo', default=0)

    class Meta:
        ordering=('produto',)
    
    def __str__(self):
        return self.produto
    
    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})
    
    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }