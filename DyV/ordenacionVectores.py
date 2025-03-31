#aplicaciones de divide y venceras para ordenar vectores

"""
Description: Algoritmo de ordenación de vectores

Este algoritmo ordena un vector de números enteros de menor a mayor utilizando el mét0do de divide y vencerás.
"""
def fusion(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

"""
Description: Algoritmo de ordenación de vectores

Este algoritmo ordena un vector de números enteros de menor a mayor utilizando el mét0do de divide y vencerás.
"""
def ordenacionVectores(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista)//2
    izquierda = ordenacionVectores(lista[:medio])
    derecha = ordenacionVectores(lista[medio:])
    return fusion(izquierda, derecha)

# Prueba
lista = [3, 1, 5, 7, 9]
print(ordenacionVectores(lista)) # [1, 3, 5, 7, 9]

# Time complexity: O(n log n)

