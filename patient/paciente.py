from person.pessoa import Pessoa

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
