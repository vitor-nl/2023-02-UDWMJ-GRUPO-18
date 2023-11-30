import pessoa

class Paciente(pessoa.Pessoa):

    def __init__(self, cpf, nome, datanasc, genero, estado, cidade, email, telefone):
        super().__init__(cpf, nome, datanasc, genero, estado, cidade, email, telefone)
        self.consulta_agendada = False
        self.dados_consulta = {}
        
    #faz o cadastro do paciente e a coleta dos dados
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

    #cria a consulta no bd
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
            
        #armazena os dados da consulta
        self.dados_consulta = { 
            'cpf_paciente': cpf_paciente,
            'local': local,
            'mes_consulta': mes_consulta,
            'dia_consulta': dia_consulta
        }

        self.consulta_agendada = True
        print("Consulta agendada com sucesso!")

    def verificar_consulta(self):
        if self.consulta_agendada:
            print("Dados da Consulta:")
            print(f"CPF do Paciente: {self.dados_consulta['cpf_paciente']}")
            print(f"Local da Consulta: {self.dados_consulta['local']}")
            print(f"Mês da Consulta: {self.dados_consulta['mes_consulta']}")
            print(f"Dia da Consulta: {self.dados_consulta['dia_consulta']}")
        else:
            print("Nenhuma consulta agendada.")