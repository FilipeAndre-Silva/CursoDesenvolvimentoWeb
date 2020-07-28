#Python If ... Else

a = 33
b = 33

if b > a:
    print("B é maior que A")
elif b == a:
    print("São iguais")
else:
    print("A é maior")

#ou
if a > b: print("a is greater than b")

#ou
print("A") if a > b else print("B")

#ou
print("A") if a > b else print("=") if a == b else print("B")

#And
x = 5
y = 10
z = 2

if x < y and z < y:
    print("IF com and")

if z < x or x < y:
    print("IF com or")

#ifas instruções não podem estar vazias, mas se, por algum motivo,
# você tiver uma ifinstrução sem conteúdo, insira-a passpara evitar erros.
if x < y:
    pass

