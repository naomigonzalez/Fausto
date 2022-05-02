# regresar = True # Este booleano sirve para controlar el flujo del programa 
# while regresar: 
#   regresar = False 
#   try: 
#     valor1 = int(input("Ingresa un valor: "))
#     valor2 = int(input("Ingresa el segundo valor: "))

#     print(valor1 + valor2) 
#   except Exception as e: 
#     print("Ingresa un número válido")
#     regresar = True 

import re 
regresar = True 
while regresar:
  regresar = False 
  valor1 = input("Ingresa un valor: ")
  valor2 = input("Ingresa el segundo valor: ")

  patron = re.compile(r'^[0-9]*$')

  if patron.match(valor1) and patron.match(valor2):
    print(f"La suma es: {int(valor1) + int(valor2)}") 

  else:
    print("Ingresa un número válido")
    regresar = True 