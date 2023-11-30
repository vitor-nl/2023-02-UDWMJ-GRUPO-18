from django.db import models

# Create your models here.

class Pessoa(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    datanasc = models.DateField()
    genero = models.CharField(max_length=10)
    endereco = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome