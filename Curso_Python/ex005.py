#Verificar String

msg = "The rain in Spain stays mainly in the plain"
x = "The" in msg
print(x)

y = "Lucas" not in msg
print(y)


#Concatenação de String

nome = "Filipe "
sobre_nome = "André"
nome_completo = nome + sobre_nome
#ou nome + " " + sobrenome
print(nome_completo)


#Formato da string

nome1 = "Minha idade é {}"
idade = 22
txt = nome1.format(idade)
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#OU

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#String com aspas duplas
txt1 = "We are the so-called \"Vikings\" from the north."
print(txt1)

