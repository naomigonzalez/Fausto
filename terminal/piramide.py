"""
4. un programa que pida un caracter y despues pida
un número y hacer una pirámide 
(x-5)
X
XX
XXX
XXXX
XXXXX

SIN GOOGLE
"""

caracter = input("Ingresa un caracter: ")
num = int(input("Ingresa un número: "))
piramide = ""
for i in range(num):
  piramide += caracter # se contatena las cadenas de texto 
  print(piramide)