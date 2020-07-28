#Coleções Python

"""
-list é uma coleção que é ordenada e mutável. Permite membros duplicados.
-tupla é uma coleção ordenada e imutável. Permite membros duplicados.
-Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
-Dictionary é uma coleção desordenada, mutável e indexada. Nenhum membro duplicado.
"""

#List
turma_A = ["Filipe","Lucas","Gabriel"]
print(turma_A)

#tupla
frutas = ("Banana","Uva","Abacaxi")
print(frutas)

#Para fazer alerações na trupla basta converter para uma lista, fazer as alteraçẽos e converter novamente para uma tupla.
"""
Para criar uma tupla com apenas um item, você precisa adicionar uma vírgula após o item,
 caso contrário, o Python não a reconhecerá como uma tupla.
"""

#Set
idades = {20,23,18}
print(type(idades))
print(idades)
#acessar elementos com um for, pois o set não tem posição fixa.
#Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.
idades.add(11)#add um item
#Para remover um item de um conjunto, use o remove(), ou o discard()método


#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Também existe um método chamado get()que fornecerá o mesmo resultado
nome = thisdict["brand"]
print(nome)

#Mudando valores
thisdict["year"] = 2018

#Acionando
thisdict["color"] = "red"

#Removendo o iten informado
#thisdict.popitem() remove o ultimo
thisdict.pop("model")




