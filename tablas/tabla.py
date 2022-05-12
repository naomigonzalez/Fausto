
# while True: # bucle 
#   numero = int(input("Ingresa un número del 1 al 100: "))

#   if numero >= 1 and numero <= 100: 
#     for i in range(10):
#       # resultado = numero * (i+1)
#       print(f"{numero} X {i+1} = {numero * (i+1)}")
#     break # rompe bucles (el while), se termina el programa 
#   else: 
#     print("Solamente números del 1 al 100")


# siempre se necesita declarar la variable antes de usarse para el bucle 
numero = 0

while numero < 1 or numero > 100: # bucle si estamos fuera del rango  
  numero = int(input("\nIngresa un número del 1 al 100: "))
 
  if numero >= 1 and numero <= 100:
    # abrir y crear un txt 
    f = open(f"tabla del {numero}.txt", "x")
    # el loop hace que sean 10 números 
    for i in range(10):
      # se escribe y se suma 1 para crear la multiplicación
      f.write(f"{numero} X {i+1} = {numero * (i+1)}\n")
      # se cierra el archivo txt
    f.close
    # condición por si se sale de tales números 
  else: 
    print("Solamente números del 1 al 100")

