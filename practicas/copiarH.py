def solve(data):
    from collections import defaultdict, deque

    # Descomponer la entrada
    N, K = data['N'], data['K']
    conexiones = data['conexiones']

    # Construir el grafo de estudiantes
    grafo = defaultdict(list)
    for u, v in conexiones:
        grafo[u].append(v)
        grafo[v].append(u)

    # Algoritmo para contar componentes conexas
    visitado = set()
    grupos = 0

    def bfs(nodo):
        cola = deque([nodo])
        visitado.add(nodo)
        while cola:
            actual = cola.popleft()
            for vecino in grafo[actual]:
                if vecino not in visitado:
                    visitado.add(vecino)
                    cola.append(vecino)

    # Contar los grupos
    for estudiante in range(N):
        if estudiante not in visitado:
            bfs(estudiante)
            grupos += 1  # Nuevo grupo encontrado

    print(grupos)


# Leer N y K
N, K = map(int, input().split())
conexiones = []

# Leer las conexiones entre estudiantes
for _ in range(K):
    u, v = map(int, input().split())
    conexiones.append((u, v))

# Agrupar en data
data = {'N': N, 'K': K, 'conexiones': conexiones}

solve(data)

#entrada1
# 10 3
# 1 4
# 1 7
# 2 9

#salida1
# 7

#entrada2 en carpeta

#salida2
# 501

#entrada3 en carpeta

#salida3
# 253

#entrada4
# 10 5
# 0 1
# 1 5
# 2 4
# 3 9
# 4 9

#salida4
# 5