class User(object):
    def __init__(self,nome_completo,cpf,telefone):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.telefone = telefone

    def exiber_dados_User(self):
        dados = """
        Nome Completo:{}
        CPF:{}
        Telefone:{}"""

        return print(dados.format(self.nome_completo,self.cpf,self.telefone))

    def upgrade_telefone(self):
        entrada = input("Digite o novo Telefone:")
        self.telefone = entrada
        return print("Telefone Autalizado ! ",self.telefone)

user1 = User("Filipe André da Silva",11129305406,81988205475)
user1.exiber_dados_User()
user1.upgrade_telefone()
user1.exiber_dados_User()