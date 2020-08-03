#Python

#Um RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
#O RegEx pode ser usado para verificar se uma sequência contém o padrão de pesquisa especificado.

import re

import re

#Pesquise a sequência para ver se começa com "The" e termina com "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! foi encontrado")
else:
  print("Não foi encontrado")

#Imprima uma lista de todas as correspondências:
#Retorne uma lista vazia se nenhuma correspondência for encontrada:
txt1 = "The rain in Spain"
y = re.findall("ai", txt1)
print(y)

#Divida em cada caractere de espaço em branco:
txt2 = "The rain in Spain"
z = re.split("\s", txt2)
print(z)

#Divida a cadeia apenas na primeira ocorrência:
txt3 = "The rain in Spain"
p = re.split("\s", txt3, 1)
print(p)

#Substitua cada caractere de espaço em branco pelo número 9
txt4 = "The rain in Spain"
m = re.sub("\s", "9", txt4)
print(m)

#Substitua as 2 primeiras ocorrências
txt5 = "The rain in Spain"
n = re.sub("\s", "9", txt5, 2)
print(n)

#Faça uma pesquisa que retornará um objeto de correspondência
txt6 = "The rain in Spain"
o = re.search("ai", txt6)
print(o)

#Imprima a posição (posição inicial e final) da primeira ocorrência de correspondência.

txt7 = "The rain in Spain"
g = re.search(r"\bS\w+", txt7)
print(g.span())

#A expressão regular procura por qualquer palavra que comece com uma letra maiúscula "S":
txt8 = "The rain in Spain"
i = re.search(r"\bS\w+", txt8)
print(i.group())