#Formatação de String Python

nome = "Filipe"
msg = "Bem vindo! {}"
print(msg.format(nome))

salario =  250
msg2 = "Salário é {:.2f}"
print(msg2.format(salario))

#Números de índice
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Índices nomeados
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))