from django.db import models
from person.models import Pessoa

# Create your models here.

# class Paciente(Pessoa):
#     consulta_agendada = models.BooleanField(default=False)
#     dados_consulta = models.JSONField(default=dict)

#     def cadastrar_paciente(self):
#         print("Bem-vindo ao cadastro de pacientes!")

#         self.cpf = input("Digite o CPF: ")
#         self.nome = input("Digite o nome: ")
#         self.datanasc = input("Digite a data de nascimento (formato DD/MM/AAAA): ")
#         self.genero = input("Digite o gênero: ")
#         self.estado = input("Digite o estado: ")
#         self.cidade = input("Digite a cidade: ")
#         self.email = input("Digite o e-mail: ")
#         self.telefone = input("Digite o telefone: ")

from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, default='Valor Padrão para CPF')
    nome = models.CharField(max_length=255, default='Valor Padrão para Nome')
    datanasc = models.DateField(default='2023-01-01')  # Substitua pela data desejada
    genero = models.CharField(max_length=20, default='Valor Padrão para Gênero')
    estado = models.CharField(max_length=255, default='Valor Padrão para Estado')
    cidade = models.CharField(max_length=100, default='Sua Cidade Padrão')
    email = models.EmailField(default='email@padrao.com')
    telefone = models.CharField(max_length=20, default='Valor Padrão para Telefone')
    consulta_agendada = models.BooleanField(default=False)
    dados_consulta = models.JSONField(default=dict)
    id = models.AutoField(primary_key=True, default=0)
