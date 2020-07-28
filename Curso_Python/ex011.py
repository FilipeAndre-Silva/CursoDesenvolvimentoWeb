#Python para loops

lista_nomes = ["Filipe","André","Silva"]

#Loop em uma lista
for x in lista_nomes:
    print(x)

#Loop em uma String
for y in "Banana":
    print(y)

#Loop com break
lista_frutas = ["Banana","Maçã","Uva","Melão"]
for z in lista_frutas:
    print(z)
    if z == "Uva":
        break

#Lopp com continue
lista_carros = ["car1","car2","car3","car4"]
for e in lista_carros:
    if e == "car2":
        continue
    print(e)

#Função range()
for t in range(5):
    print(t)

for r in range(1,5):
    print(r)

#Pulando de 2 em 2
for u in range(1,11,2):
    print(u)

#Loop com else
for c in range(6):
    print(c)
else:
    print("Fim do loop")

#Loops alinhados
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for q in adj:
  for w in fruits:
    print(q, w)

#caso precise passar um for vazio use o pass
for m in [0, 1, 2]:
  pass