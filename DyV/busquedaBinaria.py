# Description: Algoritmo de búsqueda binaria

def busquedaBinaria(lista, x):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista)//2
        if lista[medio] == x:
            return True
        else:
            if x < lista[medio]:
                return busquedaBinaria(lista[:medio], x)
            else:
                return busquedaBinaria(lista[medio+1:], x)

# Prueba
lista = [1, 3, 5, 7, 9]
x = 5
print(busquedaBinaria(lista, x)) # True