#Python Lambda
#Uma função lambda é uma pequena função anônima.

#lambda arguments : expression
x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 2))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

#Usando em uma função
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

