from django.db import models
from django.utils import timezone

class Bicicleta (models.Model):
    list_display = ['proprietario','email']
    search_fields = ['proprietario']
    fabricante = models.CharField(max_length = 45)
    cor = models.CharField(max_length = 20)
    marcha = models.BooleanField(verbose_name = 'Marcha')
    proprietario = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)

    def __str__(self):
        return self.proprietario
