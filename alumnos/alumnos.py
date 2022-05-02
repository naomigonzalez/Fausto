"""
1. guardar una lista de alumnos txt LISTO 
2. dos grupos: A y B LISTO 
	si el primer nombre del alumno empieza con 
	a - n en el grupo A 
	sino en el grupo B
3. guardar nombre y edad  LISTO 
	si el alumno es menor a 18 años, que diga "el 
	alumno es menor de edad" y en caso contrario 
	"el alumno es mayor de edad" 
4. listar los alumnos del grupo  LISTO 
*****************************************************
Número de alumno: 1
Grupo: A o B
Nombre: xxx
Edad: xxx
leyeda
*****************************************************
5. no debe terminar hasta que escribamos "finalizar" LISTO 
"""
from cmath import exp


menu = "" # cadenas 
while menu != "finalizar":
  menu = input("Seleciona una opcion: \n 1. agregar alumno \n 2. ver alumnos \n") 
  if menu == "1": 
    nombre = input("¿Cuál es el nombre del alumno? ")
    # print(len(nombre))
    if len(nombre) == 0:
      print("Ingresa un nombre válido") 
      continue #funcionan el cualquier loop 
    try:
      edad = int(input("¿Cuál es su edad? "))
    except Exception as e: 
      #print(f"Error ===> {e}")
      print("Solo se permiten números")
      continue # continue regresa al loop (línea 18) y el break rompe el bucle 


    # if nombre[0] == "a" or nombre[0] =="b" or nombre[0] =="c" or nombre[0] =="d" or nombre[0] =="e":
    #   print("Grupo A")
    # else:
    #   print("Grupo B") 
    grupoA = ["a", "b","c", "d", "e", "f","g", "h","i", "j","k", "l","m", "n"]
    grupoB = ["ñ", "o","p", "q", "r", "s","t", "u","v", "w","x", "y","z"]

  
    if edad >= 18: 
      mayorEdad ="El alumno es mayor de edad"
    else: 
      mayorEdad = "El alumno es menor de edad"


    if nombre[0].lower() in grupoA:
      f = open(f"GrupoA.txt", "a")
      f.write(f"{nombre}, {edad}, {mayorEdad} \n")
      f.close()
      
    elif nombre[0].lower() in grupoB:
      f = open(f"GrupoB.txt", "a")
      f.write(f"{nombre}, {edad}, {mayorEdad} \n")
      f.close()

    else: 
      print("No entra en ningún grupo")

    
  elif menu == "2":
    grupo = input("¿Qué grupo quieres ver? ")
    conteo = 0
    if grupo.upper() == "A": 
      with open("GrupoA.txt") as archivo:
        for linea in archivo: 
          conteo += 1
          txtspl = linea.split(",")  
          print("*****************************************************")
          print(f"Número de alumno: {conteo}")
          print("Grupo: A") 
          print(f"Nombre: {txtspl[0]}")
          print(f"Edad: {txtspl[1]}")
          print(f"{txtspl[2]}")
          print("*****************************************************")
    elif grupo.upper() == "B":
      with open("GrupoB.txt") as archivo:
        for linea in archivo:
          conteo += 1
          txtspl = linea.split(",")  
          print("*****************************************************")
          print(f"Número de alumno: {conteo}")
          print("Grupo: A") 
          print(f"Nombre: {txtspl[0]}")
          print(f"Edad: {txtspl[1]}")
          print(f"{txtspl[2]}")
    else: 
      print("No hay ningún grupo con ese nombre")

  elif menu != "finalizar": 
    print("No es válida tu respuesta ")
