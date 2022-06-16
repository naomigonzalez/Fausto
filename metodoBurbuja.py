"""
crear una FUNCION que reciba como argumento un arreglo 
de números y que los ordene de menor a mayor. 
(metodo de ordenamiento de burbuja)

def funcion(miArreglo)
  ....

nombre = [545646]
funcion(nombre)
funcion([545646], 4, 4.5, True, None) 
"""

"""
método burbuja:
consiste en comparar los elementos adyacentes los cuales
se intercambia de posición si el primer elemento es 
mayor al segundo. 

- compara en cada pasada todos los elementos sin importar si ya están or

"""

def bubbleSort(array):
  length = len(array)-1

  #bucle para las pasadas
  for i in range (0,length):
    print(f"Pasada {i+1}") 
    #comparaciones e intercambios
    for j in range (0, length):
      print(f"comparación: {array[j]} > {array[j+1]}")
      if array[j] > array[j+1]:
        print(f"intercambiar: {array[j]} x {array[j+1]}")
        aux = array[j]
        array[j] = array[j+1]
        array[j+1] = aux 
  return array 

scores = [70, 90, 0, 80, 60, 85]
print("Antes de ordenar: ")
print(scores)
print("Despues de ordenar")
print(bubbleSort(scores))


"""
resoruce: https://www.youtube.com/watch?v=nqoMzb65Ez8 
"""
