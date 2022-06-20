"""
3. pida una frase y diga cuántas vocales tiene 
"""


vocales = ["a","e","i","o","u"]

frase = input("Escriba una frase: ")
contador = 0

for i in range(len(frase)):
  # print(i) # posición en el string 
  # hola
  # print(frase[i]) "hola mundo" [55,2,8,4,994564,9]
  if frase[i] in vocales: # si la frase esta dentro de las vocales 
    contador += 1
print(f"Esta frase contiene {contador} vocales. ")
