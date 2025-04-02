def solve(itinerarios):
    resultados = []

    for itinerario in itinerarios:
        P, meses = itinerario[0], itinerario[1]
        viajes = sorted(zip(meses[::2], meses[1::2]), key=lambda x: x[1])

        max_paises = 0
        mes_actual = 0

        for inicio, fin in viajes:
            if inicio >= mes_actual:
                max_paises += 1
                mes_actual = fin

        resultados.append(str(max_paises))

    print("\n".join(resultados))


# Leer número de itinerarios
V = int(input())
itinerarios = []

for _ in range(V):
    P = int(input())  # Número de países
    meses = list(map(int, input().split()))  # Meses de llegada y salida
    itinerarios.append((P, meses))

# Ejecutar la solución
solve(itinerarios)

#entrada1
# 3
# 3
# 2 5 1 3 4 6
# 2
# 3 4 2 3
# 4
# 2 3 1 5 3 5 5 8

#salida1
# 2
# 2
# 3
