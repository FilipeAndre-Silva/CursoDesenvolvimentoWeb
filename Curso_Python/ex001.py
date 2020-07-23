import random

"""Para criar uma variável global dentro de uma função, você pode usar a global
   exemplo:
   global nome
"""
#Tipos de dados:
nome = "Filipe André"  #str
idade = 22  #int
peso = 84.5 #float
completo = 1j; #Complexo

#Conversão de tipos
x = 1
y = 2.5
z = 4j

#int para float
a = float(x)
#float para int
b = int(y)
#int para complexo
c = complex(b)
#não pode converter números complexos em outro tipo de número

#Número aleatório
aleatorio = random.randrange(1,10)
print(aleatorio)

