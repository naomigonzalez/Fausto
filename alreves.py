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
numCadena = len(frase) #10
print(numCadena)
cadenaAlReves = ""
for i in range(len(frase)): 
  numCadena -= 1
  cadenaAlReves += frase[numCadena]
  print(cadenaAlReves)

print("-"*80)
print(cadenaAlReves)


