import ast

def sumarMoneda(data):
    if isinstance(data, int):  # Caso base: un número entero
        return data, 1
    elif isinstance(data, list) and data:
        sumaElem, total = sumarMoneda(data[0])
        sumaResto, cantidadResto = sumarMoneda(data[1:])
        return sumaElem + sumaResto, total + cantidadResto
    else:
        return 0, 0  # Caso para valores no válidos o lista vacía

def abrirCofre(data):
    return sumarMoneda(data)

data = ast.literal_eval(input())
print(abrirCofre(data))

#entrada1
# [1, 2, 3]

#salida1
# (6, 3)

#entrada2
# []

#salida2
# (0, 0)

#entrada3
# [1, [2, 3], 4, [5, [6, 7], 8], 9]

#salida3
# (45, 9)