#aplicaciones de divide y venceras para ordenar vectores con pivote

def ordenarConPivote(v):
    """
    Ordena un vector de enteros utilizando el mét0do de pivote.
    """
    if len(v) <= 1:
        return v
    else:
        pivote = v[0]
        menores = []
        mayores = []
        for i in range(1, len(v)):
            if v[i] < pivote:
                menores.append(v[i])
            else:
                mayores.append(v[i])
        return ordenarConPivote(menores) + [pivote] + ordenarConPivote(mayores)

v = [3, 6, 8, 10, 1, 2, 1]
print("Vector desordenado:", v)
v_ordenado = ordenarConPivote(v)
print("Vector ordenado:", v_ordenado)

# complejidad O(n log n) en el mejor y promedio de los casos