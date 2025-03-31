def quicksort(v):
    """
    Ordena un vector de enteros utilizando el mét0do de Quicksort.
    """
    if len(v) <= 1:
        return v
    else:
        pivote = v[0]
        izq = []
        der = []
        for i in v:
            if i < pivote:
                izq.append(i)
            elif i > pivote:
                der.append(i)
            else:
                der.append(i)

        return quicksort(izq) + [pivote] + quicksort(der)

lista_no_ordenada = [3, 6, 8, 10, 1, 2, 1]
print("Lista desordenada:", lista_no_ordenada)
lista_ordenada = quicksort(lista_no_ordenada)