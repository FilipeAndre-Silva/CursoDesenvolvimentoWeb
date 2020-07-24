#Strings Python

#Função print exite o resultado no console.
print("Mensagem exibida no console")

#Atribuindo uma string a uma variavel e imprimindo no console
nome_completo = "Filipe André da Silva"
print(nome_completo)

#Outro forma de atribuir uma String
mensagem = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(mensagem)

#Strings são matrizes
msg = "Hello, World!"
#posição 1 da String
print(msg[0])

#Intervalo de caracteres
print(msg[2:5])
print(msg[-5:-2])

#Retorna o número de caracteres da string
print(len(msg))
