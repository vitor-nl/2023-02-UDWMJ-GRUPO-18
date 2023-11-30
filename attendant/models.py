from django.db import models
from person.models import Pessoa

# Create your models here.

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    datanasc = models.DateField()
    genero = models.CharField(max_length=20)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Atendente(Pessoa):
    # Se precisar adicionar campos específicos para Atendente, você pode fazer aqui.
    # Por exemplo:
    especialidade = models.CharField(max_length=100)

    def verificar_excluir_consulta(self, paciente):
        if paciente.consulta_agendada:
            print(f"Consulta agendada para o paciente {paciente.nome}:")
            paciente.verificar_consulta()

            opcao = input("Deseja excluir esta consulta? (S/N): ").upper()
            if opcao == 'S':
                paciente.consulta_agendada = False
                paciente.dados_consulta = {}
                print("Consulta excluída com sucesso.")
            else:
                print("Consulta mantida.")
        else:
            print("Paciente não possui consulta agendada.")

    def listar_consultas_agendadas(self, pacientes):
        for paciente in pacientes:
            if paciente.consulta_agendada:
                print(f"Consulta agendada para o paciente {paciente.nome}:")
                paciente.verificar_consulta()
                print()