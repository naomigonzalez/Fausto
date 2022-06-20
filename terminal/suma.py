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


# libreria de las expresiones regulares 
import re 

# se crea la varialbe para el bucle 
# es true porque si cumple con los 2 números se termina el programa 
regresar = True 
while regresar:
  # aqui cambia el bucle porque si es no son números cualquiera de los dos valores, 
  # entonces repite el ingreso de ambos valores. 
  regresar = False 
  valor1 = input("Ingresa un valor: ")
  valor2 = input("Ingresa el segundo valor: ")

  # operaciones con expresiones regulares 
  patron = re.compile(r'^[0-9]*$')

  # aqui se valida si ambos valores son números, 
  # si sí lo son, imprime la suma 
  if patron.match(valor1) and patron.match(valor2):
    print(f"La suma es: {int(valor1) + int(valor2)}") 

  # si no son números imprime que no es válido y el bucle vuelve
  else:
    print("Ingresa un número válido\n")
    regresar = True 