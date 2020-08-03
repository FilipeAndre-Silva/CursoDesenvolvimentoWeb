#Python Math

#O Python possui um conjunto de funções matemáticas integradas,
# incluindo um extenso módulo de matemática, que permite executar tarefas matemáticas em números.

#As funções min()e max()podem ser usadas para encontrar o valor mais baixo ou mais alto em um iterável:

#Retornando valor maior e menor
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#Retorna o valor absoluto
z = abs(-7.25)
print(z)

#Retorna a potência
b = pow(4, 3)
print(b)

# Python também possui um módulo interno chamado math, que estende a lista de funções matemáticas.

import math

#Retorna a raiz quadrada
t = math.sqrt(64)
print(t)

#Formas de retornar arrendondamento
k = math.ceil(1.4) #método arredonda um número para cima até o número inteiro mais próximo
j = math.floor(1.4)#arredonda um número para baixo para o número inteiro mais próximo e retorna o resultado
print(k)
print(j)

#Retorna o valor de PI
r = math.pi
print(r)