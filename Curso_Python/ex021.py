#Escopo do Python

#Uma variável criada dentro de uma função
# está disponível dentro dessa função:
def myfunc():
  x = 300
  print(x)

myfunc()


#use a global palavra - chave se desejar alterar uma variável global dentro de uma função.
y = 300
def myfunc2():
  global y
  y = 200

myfunc2()
print(y)

