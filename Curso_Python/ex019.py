class ContaBancaria(object):

    def __init__(self,saldo):
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo = self.saldo + valor
        self.exibir_saldo()

    def sacar(self,valor):
        self.saldo = self.saldo - valor
        self.exibir_saldo()

    def exibir_saldo(self):
        print("Saldo da Conta Bancaria",self.saldo)

class ContaCorrente(ContaBancaria):
    pass

class ContaPoupança(ContaBancaria):
    def __init__(self, saldo):
        ContaBancaria.__init__(self, saldo)
        self.rentabilidade = 0.5
        print("Conta Poupança Aberta !")
        print("Saldo inicial da conta:",saldo)
        print("#"* 35)

    def depositar(self,valor):
        print("Deposito de :",valor)
        self.saldo = self.saldo + valor
        if valor > 1000:
            self.add_rentabilidade()
            self.exibir_saldo()
        else:
            self.exibir_saldo()

    def sacar(self,valor):
        print("Creditado:",valor)
        self.saldo = self.saldo - valor
        self.exibir_saldo()

    def exibir_saldo(self):
        return print("Saldo da Conta Poupança:",self.saldo, "/ Rentabilidade",self.rentabilidade)

    def add_rentabilidade(self):
        self.rentabilidade = self.rentabilidade + 0.5


x = ContaCorrente(100)
x.sacar(5)

