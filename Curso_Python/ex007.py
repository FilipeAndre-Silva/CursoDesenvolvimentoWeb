#Operadores Python
"""
Operadores aritméticos
Operadores de atribuição
Operadores de comparação
Operadores lógicos
Operadores de identidade
Operadores de associação
Operadores bit a bit

"""
#Operadores aritméticos de Python
x = 10
y = 5

x + y
x - y
x * y
x / y
x % y #resto da divisão
x ** y #Exponenciação
x // y #arredonda o resultado para o número inteiro mais próximo


#Operadores de atribuição do Python(Se aplica a todos os operadores)
x = x + 3
#ou
x += 3

x = x - 3
#ou
x -= 3


#Operadores de comparação Python
x = 10
y = 5

x == y
x != y
x > y
x < y
x >= y
x <= y

#Operadores lógicos Python

x = 5
#and
print(x > 3 and x < 10)

#or
print(x > 3 or x < 4)

#not
print(not(x > 3 and x < 10))


#Operadores de identidade Python
#Os operadores de identidade são usados ​​para comparar os objetos, não se forem iguais, mas se
#forem realmente o mesmo objeto, com o mesmo local de memória
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
#is
print(x is z)
#is not
print(x is not z)



