
# while True: # bucle 
#   numero = int(input("Ingresa un número del 1 al 100: "))

#   if numero >= 1 and numero <= 100: 
#     for i in range(10):
#       # resultado = numero * (i+1)
#       print(f"{numero} X {i+1} = {numero * (i+1)}")
#     break # rompe bucles (el while), se termina el programa 
#   else: 
#     print("Solamente números del 1 al 100")

numero = 0

while numero < 1 or numero > 100: # bucle si estamos fuera del rango  
  numero = int(input("Ingresa un número del 1 al 100: "))
 
  if numero >= 1 and numero <= 100:
    f = open(f"tabla del {numero}.txt", "x")
    for i in range(10):
      f.write(f"{numero} X {i+1} = {numero * (i+1)}\n")
    f.close
  else: 
    print("Solamente números del 1 al 100")

