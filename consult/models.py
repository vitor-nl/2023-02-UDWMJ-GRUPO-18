from django.db import models
from person.models import Pessoa

# Create your models here.

class Consulta(Pessoa):
    consulta_agendada = models.BooleanField(default=False)
    cpf_paciente = models.CharField(max_length=14)
    local = models.CharField(max_length=50)
    mes_consulta = models.IntegerField()
    dia_consulta = models.IntegerField()

    def criar_consulta(self):
        print(f"Bem-vindo, {self.nome}!")
        cpf_paciente = input("Por favor, confirme o seu CPF: ")
        while cpf_paciente != self.cpf:
            cpf_paciente = input("CPF incorreto, digite novamente: ")

        print("Escolha um local para a sua consulta:")
        print("1 - Hospital Moinhos de Vento")
        print("2 - Hospital Cristo Redentor")
        print("3 - Santa Casa de Misericórdia")

        local = input("Opção: ")

        mes_consulta = int(input("Escolha o mês da sua consulta (1 - 12): "))
        while not (1 <= mes_consulta <= 12):
            mes_consulta = int(input("Mês inválido, escolha o mês da sua consulta (1 - 12): "))

        dia_consulta = int(input("Escolha o dia da sua consulta (1 - 31): "))
        while not (1 <= dia_consulta <= 31):
            dia_consulta = int(input("Dia inválido, escolha um dia para a sua consulta (1 - 31): "))
            
        # Armazena os dados da consulta
        self.consulta_agendada = True
        self.cpf_paciente = cpf_paciente
        self.local = local
        self.mes_consulta = mes_consulta
        self.dia_consulta = dia_consulta
        print("Consulta agendada com sucesso!")

    def verificar_consulta(self):
        if self.consulta_agendada:
            print("Dados da Consulta:")
            print(f"CPF do Paciente: {self.cpf_paciente}")
            print(f"Local da Consulta: {self.local}")
            print(f"Mês da Consulta: {self.mes_consulta}")
            print(f"Dia da Consulta: {self.dia_consulta}")
        else:
            print("Nenhuma consulta agendada.")