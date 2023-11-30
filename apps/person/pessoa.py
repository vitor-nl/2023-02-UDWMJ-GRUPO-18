from django.urls import path, include
from . import views
from rest_framework import routers
from django.db import models

app_name = 'person'

router = routers.DefaultRouter()
router.register('pessoa', views.CategoryViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls) )
]

class Pessoa(models.Model):
    cpf = models.CharField('CPF', max_length=14, unique=True)
    nome = models.CharField('Nome', max_length=100)
    datanasc = models.DateField('Data de Nascimento')
    genero = models.CharField('Gênero', max_length=10)
    endereco = models.CharField('Endereço', max_length=255)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    senha = models.CharField('Senha', max_length=50)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return self.nome
        
    # def mudar_senha(self):
    #     nova_senha = input("Digite a nova senha: ")
    #     self.senha = nova_senha
    #     print("Sua senha foi alterada com sucesso, nova senha: ", self.senha)
        