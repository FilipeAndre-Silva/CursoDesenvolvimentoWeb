#Importando o módulo criado
from mymodule import bem_vindas
import mymodule as i #abreviando modulo

nome = str(input("Digite seu nome: "))
bem_vindas(nome)

#Acessando variaveis
x = i.person1["name"]
print(x)

#unção interna para listar todos os nomes de funções (ou nomes de variáveis) em um módulo
lista_funcao = dir(i)
print(lista_funcao)


