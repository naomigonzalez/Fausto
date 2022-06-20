"""
un programa que pida una frase al usuario y que se imprima al reves
"""
# import re

# pat = re.compile("\w+")
# print(pat.findall("¡Hola, Mundo!"))

# def invert(m):
#     return m.group(0)[::-1]

# resultado = pat.sub(invert, "¡Hola, Mundo!")
# print(resultado)

# frase = input("Escriba una frase: ")
# print((frase) [::-1])
# nombre = "Pancho"
# variable = f"hola {nombre}"
# print(variable)


frase = input("Escriba una frase: ")
# variable almacenar el número total que tiene de caracteres
numCadena = len(frase) #10
print(numCadena)
# variable vacia para almacenar la frase al reves
cadenaAlReves = ""

for i in range(len(frase)): 
  # restarle la posición 
  numCadena -= 1 #"hola" ['h', 'o', 'l', 'a'] -><- [0, 1, 2, 3]
  cadenaAlReves += frase[numCadena]
  print(cadenaAlReves)

print("-"*80)
print(cadenaAlReves)


