"""
2. hacer una función que reciba 3 números (que pida
por consola) de esos tres números cuál es el mínimo
"""
regresar = True

def compararNumeros(num1, num2):
  if num1 < num2:
    return num1 
  return num2

while regresar:
  regresar = False 
  try: 
    num1 = int(input("Ingresa el valor 1: "))
    num2 = int(input("Ingresa el valor 2: "))
    num3 = int(input("Ingresa el valor 3: "))

    numeroMenor = compararNumeros(num1, num2)
    numeroMenor = compararNumeros(numeroMenor, num3)

    print(f"El número menor es {numeroMenor}")

  except Exception as e: 
    print("Ingresa un valor númerico")
    regresar = True 

