from django.db import models
from person.models import Pessoa

# Create your models here.

class Paciente(Pessoa):
    consulta_agendada = models.BooleanField(default=False)
    dados_consulta = models.JSONField(default=dict)

    def cadastrar_paciente(self):
        print("Bem-vindo ao cadastro de pacientes!")

        self.cpf = input("Digite o CPF: ")
        self.nome = input("Digite o nome: ")
        self.datanasc = input("Digite a data de nascimento (formato DD/MM/AAAA): ")
        self.genero = input("Digite o gênero: ")
        self.estado = input("Digite o estado: ")
        self.cidade = input("Digite a cidade: ")
        self.email = input("Digite o e-mail: ")
        self.telefone = input("Digite o telefone: ")