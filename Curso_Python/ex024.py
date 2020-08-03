#Python JSON
#O Python possui um pacote interno chamado json, que pode ser usado para trabalhar com dados JSON.

import json
#Converter de JSON em Python:

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o json.dumps()método
# a Python object (dict):
z = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(z)

# the result is a JSON string:
print(y)

#Converta objetos Python em strings JSON e imprima os valores:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



