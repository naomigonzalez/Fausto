"""
hacer un programa que pida un número del 0 al 100 
al usuario. Y que genere números aleatorios del 0 al 100
y que no se detenga hasta que encuentre el numero 
del usuario (que los vaya imprimiendo) y al final imprimir
cuantos números genero 
# """
# import random

# guess_number = int(input("Elige un número del 0 al 100: "))

# num_random = -1
# contador = 0
# suma = 0

# while num_random != guess_number:
#   num_random = random.randint(0, 100)
#   print(num_random)
#   contador += num_random
#   suma += num_random

#   if num_random == guess_number: 
#     print("congrats!")
#     print(f"encontré el número {guess_number} en {contador} intentos y la suma es {suma}")

variable1 = 5 == 30 #false
variable2 = False #false
variable3= "Nao" == "Nao" #false
variable4 = -4
variable4 *= -1

#        false      
if not (variable1 and (variable2 or variable3) and variable4 >= 0):
  print("entro")
else:
  print("No entro")

