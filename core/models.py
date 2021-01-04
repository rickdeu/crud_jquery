from django.db import models

class Alvo(models.Model):

    nome_alvo = models.CharField(
        max_length=100, 
        verbose_name='Nome',
        null=False,
        blank=False,
        help_text='Informe o nome'
        )
    lat = models.CharField(
        max_length=100, 
        verbose_name='Latitude',
        null=False,
        blank=False,
        help_text='Latitude'
        )
    lon = models.CharField(
        max_length=100, 
        verbose_name='Longitude',
        null=False,
        blank=False,
        help_text='Longitude'
        )
    data_expiracao = models.DateField(
        max_length=100, 
        verbose_name='Data de expiração',
        null=False,
        blank=False,
        help_text='Informe a data de expiração'
        )
        

    def __str__(self):
        return self.nome_alvo
    class Meta:
        verbose_name = 'Alvo'
        verbose_name_plural = 'Alvos'
        ordering = ['-nome_alvo']
