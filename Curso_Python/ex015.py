#Classes e objetos Python

#Criar uma classe
class MyClass:
    x = 5

#Criar Objeto
objeto1 = MyClass()

#Exibindo seu atributo
print(objeto1.x)

#Uso do __init__
#Todas as classes têm uma função chamada __init __ (), que é sempre executada quando a classe está sendo iniciada.
#Use a função __init __ () para atribuir valores às propriedades do objeto ou outras operações necessárias quando
# o objeto estiver sendo criado
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def msg_apresentacao(self):
        return print("Olá! meu nome é " + self.nome)


pessoa1 = Pessoa("Filipe",23)
print(pessoa1.nome)
print(pessoa1.idade)
pessoa1.msg_apresentacao()

#Modificar propriedades do objeto
#pessoa1.idade = 25

#Excluir propriedades do objeto
#del pessoa1.idade

#Excluir objetos
#del pessoa1

#Uma class sem conteúdo, insira a passinstrução para evitar erros.
"""
class Person:
  pass
"""


