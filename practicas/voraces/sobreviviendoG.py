def solve(data):
    from collections import defaultdict

    # Descomponer la entrada
    N, K = data['N'], data['K']
    relaciones = data['relaciones']

    # Ordenar las relaciones por esfuerzo ascendente (para Kruskal)
    relaciones.sort(key=lambda x: x[2])

    # Estructuras para Kruskal
    parent = list(range(N))
    rank = [0] * N
    esfuerzo_concursante = defaultdict(int)
    esfuerzo_total = 0

    # Funciones auxiliares para el algoritmo de Kruskal (Union-Find)
    def find(nodo):
        if parent[nodo] != nodo:
            parent[nodo] = find(parent[nodo])
        return parent[nodo]

    def union(nodo1, nodo2):
        raiz1, raiz2 = find(nodo1), find(nodo2)
        if raiz1 != raiz2:
            if rank[raiz1] > rank[raiz2]:
                parent[raiz2] = raiz1
            elif rank[raiz1] < rank[raiz2]:
                parent[raiz1] = raiz2
            else:
                parent[raiz2] = raiz1
                rank[raiz1] += 1
            return True
        return False

    # Aplicar Kruskal para construir el árbol de expansión mínima
    for u, v, w in relaciones:
        if union(u, v):
            esfuerzo_concursante[u] += w
            esfuerzo_concursante[v] += w
            esfuerzo_total += w

    # Generar la salida en orden lexicográfico
    for i in sorted(esfuerzo_concursante.keys()):
        print(f"C{i} -> {esfuerzo_concursante[i]}")

    print(f"Esfuerzo realizado -> {esfuerzo_total}")


# Leer N y K
N, K = map(int, input().split())
relaciones = []

# Leer las relaciones
for _ in range(K):
    u, v, w = map(int, input().split())
    relaciones.append((u, v, w))

# Agrupar en data
data = {'N': N, 'K': K, 'relaciones': relaciones}

solve(data)

#entrada1
# 10 13
# 0 2 68
# 0 8 63
# 1 4 53
# 1 7 110
# 2 7 11
# 3 5 107
# 3 9 30
# 4 7 97
# 5 7 38
# 5 9 31
# 6 8 67
# 7 8 24
# 7 9 41

#salida1
# C0 -> 63
# C1 -> 53
# C2 -> 11
# C3 -> 30
# C4 -> 150
# C5 -> 69
# C6 -> 67
# C7 -> 170
# C8 -> 154
# C9 -> 61
# Esfuerzo realizado -> 414

#entrada2
# 10 19
# 0 1 140
# 0 6 133
# 0 8 34
# 0 9 163
# 1 3 74
# 1 6 98
# 1 7 186
# 2 4 145
# 2 6 113
# 2 7 88
# 2 8 22
# 3 6 138
# 3 9 52
# 4 5 64
# 4 9 189
# 5 7 166
# 5 9 101
# 6 7 91
# 6 9 184

#salida2
# C0 -> 34
# C1 -> 172
# C2 -> 110
# C3 -> 126
# C4 -> 64
# C5 -> 165
# C6 -> 189
# C7 -> 179
# C8 -> 56
# C9 -> 153
# Esfuerzo realizado -> 624

#entrada3
# 10 21
# 0 1 183
# 0 3 133
# 0 4 57
# 0 5 176
# 0 7 105
# 0 8 55
# 1 5 18
# 1 7 67
# 2 5 54
# 2 6 23
# 2 8 79
# 2 9 207
# 3 5 46
# 3 6 51
# 3 7 168
# 3 8 19
# 4 5 91
# 4 8 146
# 5 6 205
# 5 8 147
# 6 9 42

#salida3
# C0 -> 112
# C1 -> 85
# C2 -> 23
# C3 -> 116
# C4 -> 57
# C5 -> 64
# C6 -> 116
# C7 -> 67
# C8 -> 74
# C9 -> 42
# Esfuerzo realizado -> 378

#entrada4 en carpeta de pruebas