"""
1. hacer una función que reciba 2 números (que pida
por consola) de esos tres números cuál es el 
más grande 
SIN GOOGLE 
"""
"""
entero = 10 # int - integer
punto_flotante = 10.0 # float - double - punto flotante
boleano = True # booleano
none = None # null no existe la variable en memoria
String = "cadena de texto45454"
"""

def compararNumeros(num1, num2):
  if num1 > num2:
    return num1 
  # cuando no se cumple lo del if (identado) se salta a la siguiente linea 
  return num2  

regresar = True 
while regresar: # en los if, while siempre se valida una condicion (4 > 4) False
  regresar = False #es el indicador para que no sea un loop infinito 
  try: 
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))
    numMayor = compararNumeros(num1, num2)
    numMayor = compararNumeros(numMayor, num3)
    print(f"El numero mayor es: {numMayor}")
    # if num2 < num1 > num3: 
    #   print(f"{num1} es el número más grande")  

    # elif num1 < num2 > num3:
    #   print(f"{num2} es el número más grande")

    # elif num1 < num3 > num2:
    #   print(f"{num3} es en número más grande")
    # else:
    #   print("Intenta de nuevo")
    #   regresar = True
  except Exception as e:
    print("Ese no es un valor válido")
    regresar = True 
    




