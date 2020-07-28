#Funções Python

def msg_sorte():
    print("Olá mundo")

msg_sorte()

#Função passando argumentos
def msg_boasVindas(entrada):
    print(entrada + " Seja Bem Vindo(a)!")

entrada = input("Digite seu nome: ")
msg_boasVindas(entrada)

#Quando não sabemos quandos argumentos vão ser passados para a função usamos o Argumentos arbitrários, * args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Enviando arqumentos como chave
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Se o número de argumentos da palavra-chave for desconhecido, adicione um duplo **antes do nome do parâmetro:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#usar um valor de parâmetro padrão
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passando uma lista como argumento
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#se, por algum motivo, tiver uma function sem conteúdo, insira a pass
def myfunction():
  pass