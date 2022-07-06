def bubbleSort(array):
  length = len(array)-1

  #bucle para las pasadas
  for i in range (0,length):
    # print(f"Pasada {i+1}") 
    #comparaciones e intercambios
    for j in range (0, length):
  #     print(f"comparación: {array[j]} > {array[j+1]}")
      if array[j] > array[j+1]:
  #       print(f"intercambiar: {array[j]} x {array[j+1]}")
        aux = array[j]
        array[j] = array[j+1]
        array[j+1] = aux 
  return array 

scores = [70, 90, 0, 80, 60, 85]
# print("Antes de ordenar: ")
# print(scores)
# print("Despues de ordenar")
print(bubbleSort(scores))
print(f"Número máximo: {bubbleSort(scores)[0]}")
print(f"Número mínimo: {bubbleSort(scores)[5]}")



"""
resoruce: https://www.youtube.com/watch?v=nqoMzb65Ez8 
"""
print("-------------------------------------------")

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoBurbuja(unaLista)
print(unaLista)