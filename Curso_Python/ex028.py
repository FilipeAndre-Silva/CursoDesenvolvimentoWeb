#Tratamento de Erros e Exceções

try: # Tente
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

except (ValueError,TypeError):
    print("Tivemos um problema com os tipos de dados que foram digitados")
except ZeroDivisionError:
    print("Não pode dividir por zero !")
except KeyboardInterrupt:
    print("Não foi digitado nada")
except Exception as erro:
    print(f"Erro {erro.__class__}")
else: #Caso não de erro
    print(f"O resultado é {r}")
finally: #Executado de qualquer forma
    print("Volte sempre!, muito obrigado! ")