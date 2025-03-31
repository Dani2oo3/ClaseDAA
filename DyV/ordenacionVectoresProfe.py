def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        mitad = len(v) // 2
        izq = mergesort(v[:mitad])
        der = mergesort(v[mitad:])
        return merge(izq, der)

def merge(izq, der):
    i = 0
    j = 0
    result = []

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            result.append(izq[i])
            i += 1
        else:
            result.append(der[j])
            j += 1

    result.extend(izq[i:])
    result.extend(der[j:])

    return result

# Ejemplo de uso
v = [5, 2, 9, 1, 5, 6]
print("Vector original:", v)
v_ordenado = mergesort(v)
print("Vector ordenado:", v_ordenado)

