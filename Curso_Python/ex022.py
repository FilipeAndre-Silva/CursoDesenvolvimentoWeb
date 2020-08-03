#Pyhton Data

import datetime

#Exibir data atual
x = datetime.datetime.now()
print(x)

#Exibir dia e semana:
y = datetime.datetime.now()
print(y.year)
print(y.strftime("%A"))

#Criando um objeto de data
z = datetime.datetime(2020, 5, 17)
print(z)

#O método é chamado strftime()e usa um parâmetro format,
# para especificar o formato da string retornada:

p = datetime.datetime(2018, 6, 1)
print(p.strftime("%Uma referência de todos os códigos de formato legal:B"))

#Uma referência de todos os códigos de formato legal é o link:
#https://www.w3schools.com/python/python_datetime.asp
#lista de retornos de data possiveis com strftime()