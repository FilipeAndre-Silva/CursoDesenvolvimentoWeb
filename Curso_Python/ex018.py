class ContaBancaria(object):
    def __init__(self,numero_conta,saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo = self.saldo + valor
        return self.consulta_sald()

    def sacar(self,valor):
        self.saldo = self.saldo - valor
        return self.consulta_sald()

    def consulta_sald(self):
        print("Valor atual na conta:", self.saldo)


