from person.pessoa import Pessoa

class Atendente(Pessoa):
    
    def __init__(self, cpf, nome, datanasc, genero, estado, cidade, email, telefone):
        super().__init__(cpf, nome, datanasc, genero, estado, cidade, email, telefone)

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