grupoA = ["a", "b","c", "d", "e", "f","g", "h","i", "j","k", "l","m", "n"]
grupoB = ["ñ", "o","p", "q", "r", "s","t", "u","v", "w","x", "y","z"]

def crear_archivo(grupo, linea):
  f = open(f"Grupo{grupo}.txt", "a")
  f.write(linea) 
  f.close()

def grupoElegido(grupoAElegir, linea):
  f = open(f"Grupo{grupoAEligir}.txt", "a")
  f.write(linea) 
  f.close()

def imprimir_info(conteo, txtspl, grupo):
  print(f"""
        *****************************************************
        Número de alumno: {conteo}
        Grupo: {grupo}
        Nombre: {txtspl[0]}
        Edad: {txtspl[1]}
        {txtspl[2]}
        *****************************************************
          """)
          

menu = "" # cadenas 
while menu != "finalizar":
  menu = input("Seleciona una opcion: \n 1. agregar alumno \n 2. ver alumnos \n 3. buscar \n") 
  if menu == "1": 
    nombre = input("¿Cuál es el nombre del alumno? ")
    if len(nombre) == 0:
      print("Ingresa un nombre válido") 
      continue #funcionan el cualquier loop 
    try:
      edad = int(input("¿Cuál es su edad? "))
    except Exception as e: 
      print("Solo se permiten números")
      continue # continue regresa al loop (línea 18) y el break rompe el bucle 
 
    mayorEdad = "El alumno es mayor de edad" if edad >= 18 else "El alumno es menor de edad" # ternario 
    #mayorEdad = (edad>=18)?"El alumno es mayor de edad":"El alumno es menor de edad" ternario javascript


    if nombre[0].lower() in grupoA:
      crear_archivo("A", f"{nombre}, {edad}, {mayorEdad} \n")
    elif nombre[0].lower() in grupoB:
      crear_archivo("B", f"{nombre}, {edad}, {mayorEdad} \n")
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
          imprimir_info(conteo, txtspl, "A")
    elif grupo.upper() == "B":
      with open("GrupoB.txt") as archivo:
        for linea in archivo:
          conteo += 1
          txtspl = linea.split(",") 
          imprimir_info(conteo, txtspl, "B") 
    else: 
      print("No hay ningún grupo con ese nombre")

  elif menu == "3": 
    grupoAEligir = input("¿qué grupo quieres buscar? ")
    if grupoAEligir != "A" and grupoAEligir != "B": 
      print("Elige solo A o B ")
    else:
      opciones = input("¿Qué quieres buscar? \n 1. nombre \n 2. edad \n 3. mayor de edad \n 4. menor de edad ")
      if opciones == "1": 
        nombre_buscar = input("¿Qué nombre quieres buscar?")
        with open("GrupoA.txt") as archivo:
          for linea in archivo: #"bere, 65, El alumno es mayor de edad "
            buscar = linea.split(",")
            if nombre_buscar == buscar[0]:
              print(f" encontrado {buscar[0]}")

  

  elif menu != "finalizar": 
    print("No es válida tu respuesta ")
