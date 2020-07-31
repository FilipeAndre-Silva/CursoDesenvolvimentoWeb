#Python Iterators

#Retorne um iterador de uma tupla e imprima cada valor:
mytuple = ("Filipe","André","Silva")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mtstr = "Filipe"
myit_letra = iter(mtstr)
print(next(myit_letra))
print(next(myit_letra))
print(next(myit_letra))
print(next(myit_letra))
print(next(myit_letra))
print(next(myit_letra))

mytuple2 = ("apple", "banana", "cherry")
for x in mytuple2:
  print(x)

mystr2 = "banana"
for x in mystr2:
  print(x)

#Criando uma classe de interador
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
