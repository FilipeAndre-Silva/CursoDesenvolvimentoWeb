#Tratamento de Erros e Exceções

try: # Tente
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro: #Caso de erro
    print("Infelizmente tivemos um problema :(")
    print(f"Erro encontrado: {erro.__class__}")
else: #Caso não de erro
    print(f"O resultado é {r}")
finally: #Executado de qualquer forma
    print("Volte sempre!, muito obrigado! ")