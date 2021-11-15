from django.db import models
from django.db.models.base import Model

class TimeStampedModel(models.Model):
    """Criado em - Atualiza a data e a hora quando cria
    modificado em - Atualiza a data e a hora quando sofre auterações """
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract =True
        
