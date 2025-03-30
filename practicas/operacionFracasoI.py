from collections import defaultdict, deque

def solve(data):
    """
    Ejecuta BFS para calcular cuántos fans están alcanzables hasta el nivel M.
    """
    M, K, C = data['M'], data['K'], data['C']
    relaciones = data['relaciones']

    # Construcción del grafo como diccionario de conjuntos
    grafo = defaultdict(set)
    for u, v in relaciones:
        grafo[u].add(v)
        grafo[v].add(u)

    # BFS desde el nodo 0
    visitado = set()
    cola = deque([0])  # Empezamos desde el nodo 0
    nivel = 0  # Nivel inicial

    while cola and nivel < M:
        for dato in range(len(cola)):
            actual = cola.popleft()
            if actual not in visitado:
                visitado.add(actual)
                cola.extend(grafo[actual])
        nivel += 1

    print(len(visitado))  # Cantidad de nodos alcanzables

# Leer N (cantidad de concursantes o casos de prueba)
N = int(input().strip())

for _ in range(N):
    # Leer M, K y C
    M, K, C = map(int, input().strip().split())
    relaciones = [tuple(map(int, input().strip().split())) for _ in range(C)]

    # Agrupar en data
    data = {'M': M, 'K': K, 'C': C, 'relaciones': relaciones}

    # Resolver el caso actual
    solve(data)

#entrada1
# 1
# 2 8 7
# 0 1
# 0 2
# 1 3
# 1 4
# 1 5
# 2 6
# 6 7

#salida1
# 3

#entrada2
# 0

#salida2

#entrada3
# 1
# 3 8 7
# 0 1
# 0 2
# 1 3
# 1 4
# 1 5
# 2 6
# 6 7

#salida3
# 7

#entrada4 en carpeta

#salida4
# 30
# 30
# 15
# 30
# 15
# 30

