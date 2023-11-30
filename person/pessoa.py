class Pessoa():
    def __init__(self, cpf, nome, datanasc, genero, endereco, email, telefone, senha):
        self.cpf = cpf
        self.nome = nome
        self.datanasc = datanasc
        self.genero = genero
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        self.senha = senha
        
    # def mudar_senha(self):
    #     nova_senha = input("Digite a nova senha: ")
    #     self.senha = nova_senha
    #     print("Sua senha foi alterada com sucesso, nova senha: ", self.senha)