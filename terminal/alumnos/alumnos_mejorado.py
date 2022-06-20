grupoA = ["a", "b","c", "d", "e", "f","g", "h","i", "j","k", "l","m", "n"]
grupoB = ["ñ", "o","p", "q", "r", "s","t", "u","v", "w","x", "y","z"]

def crear_archivo(grupo, linea):
  f = open(f"Grupo{grupo}.txt", "a")
  f.write(linea) 
  f.close()

def imprimir_info(conteo, data, grupo):
  print(f"""
        *****************************************************
        Número de alumno: {conteo}
        Grupo: {grupo}
        Nombre: {data[0]}
        Edad: {data[1]}
        {data[2]}
        *****************************************************
          """)


def lee_archivo(grupoAElegir): 
  informacion_del_archivo = []
  with open(f"Grupo{grupoAElegir}.txt") as archivo:
    for linea in archivo: #"bere, 65, El alumno es mayor de edad "
      informacion_del_archivo.append(linea)
  return informacion_del_archivo
           

menu = "" # cadenas 
while menu != "finalizar":
  menu = input("Seleciona una opcion: \n 1. agregar alumno \n 2. ver alumnos \n") 
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
      for linea in lee_archivo("A"): 
        conteo += 1# "bere, 65, El alumno es mayor de edad "
        # ['bere', '65', 'El alumno es mayor de edad']
        #     0      1         2
        texto_separado = linea.split(",")  
        imprimir_info(conteo, texto_separado, "A")
    elif grupo.upper() == "B":
      for linea in lee_archivo("B"):
        conteo += 1
        texto_separado = linea.split(",") 
        imprimir_info(conteo, texto_separado, "B") 
    else: 
      print("No hay ningún grupo con ese nombre")
  elif menu == "3": 
    grupoAElegir = input("¿qué grupo quieres buscar? ")
    if grupoAElegir != "A" and grupoAElegir != "B": 
      print("Elige solo A o B ")
    else:
      opciones = input("¿Qué quieres buscar? \n 1. nombre \n 2. edad \n 3. mayor de edad \n 4. menor de edad ")
      if opciones == "1": 
        nombre_buscar = input("¿Qué nombre quieres buscar?")
        """[
          "bere, 65, El alumno es mayor de edad ", 0
          "bere, 65, El alumno es mayor de edad ",1
          "bere, 65, El alumno es mayor de edad ",2
          "bere, 65, El alumno es mayor de edad ",3
          "Fausto, 85, El alumno es mayor de edad ",4
          "alberto, 74, El alumno es mayor de edad ",5
          "bere, 65, El alumno es mayor de edad ",6
        ]"""
        for linea in lee_archivo(grupoAElegir): #"bere, 65, El alumno es mayor de edad "
          buscar = linea.split(",")
          if nombre_buscar == buscar[0]:
            print(f" encontrado {buscar[0]}")
      elif opciones == "2": 
        nombre_buscar = input("¿Qué edad quieres buscar?")
        for linea in lee_archivo(grupoAElegir): #"bere, 65, El alumno es mayor de edad "
          buscar = linea.split(",")
          if nombre_buscar == buscar[1]:
            print(f" encontrado {buscar[1]}")
      elif opciones == "3":
        contador = 0 
        for linea in lee_archivo(grupoAElegir): #"bere, 65, El alumno es mayor de edad "
          buscar = linea.split(",")
          if buscar[2].find("mayor") >= 0:
            contador += 1
            imprimir_info(contador, buscar, grupoAElegir) 

      elif opciones == "4":
        contador = 0 
        for linea in lee_archivo(grupoAElegir): #"bere, 65, El alumno es mayor de edad "
          buscar = linea.split(",")
          #if "El alumno es mayor de edad" == buscar[2]:
          if buscar[2].find("menor") >= 0:
            contador += 1
            imprimir_info(contador, buscar, grupoAElegir) 
          
           

  elif menu != "finalizar": 
    print("No es válida tu respuesta ")
