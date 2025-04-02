import heapq

def solve(data):
    N, M = data['N'], data['M']
    graph = {i: [] for i in range(N)}

    for c1, c2, d in data['conexiones']:
        graph[c1].append((c2, d))
        graph[c2].append((c1, d))

    S, E = data['S'], data['E']

    # Algoritmo de Dijkstra usando heapq
    pq = [(0, S)]  # (distancia acumulada, nodo actual)
    distances = {i: float('inf') for i in range(N)}
    distances[S] = 0
    previous = {i: None for i in range(N)}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == E:
            break

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    if distances[E] == float('inf'):
        print("-1")  # No hay camino
        return

    # Reconstrucción del camino
    path = []
    node = E
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()

    print(distances[E])
    print(" ".join(map(str, path)))


# Entrada
N, M = map(int, input().split())
conexiones = [tuple(map(int, input().split())) for _ in range(M)]
S, E = map(int, input().split())

data = {'N': N, 'M': M, 'conexiones': conexiones, 'S': S, 'E': E}
solve(data)

#entrada1
# 9 14
# 0 1 4
# 0 7 8
# 1 2 8
# 1 7 11
# 2 3 7
# 2 5 4
# 2 8 2
# 3 4 9
# 3 5 14
# 4 5 10
# 5 6 2
# 6 7 1
# 6 8 6
# 7 8 7
# 0 4

#salida1
# 21
# 0 7 6 5 4

#entrada2
# 20 33
# 0 11 34
# 0 18 38
# 1 3 88
# 1 5 88
# 1 17 24
# 1 19 84
# 2 12 30
# 2 16 86
# 2 17 19
# 3 9 29
# 3 14 83
# 3 16 94
# 3 17 24
# 4 6 17
# 4 8 10
# 6 10 69
# 6 13 28
# 7 10 96
# 7 12 38
# 7 13 4
# 7 14 56
# 8 14 17
# 10 13 88
# 10 14 78
# 10 15 2
# 11 16 36
# 11 19 19
# 12 13 11
# 12 14 34
# 12 16 58
# 13 17 96
# 13 19 56
# 15 17 18
# 8 11

#salida2
# 130
# 8 4 6 13 19 11

#entrada3
# 20 59
# 0 9 30
# 0 10 63
# 0 14 97
# 1 3 71
# 1 5 73
# 1 16 55
# 1 18 86
# 1 19 47
# 2 5 56
# 2 6 82
# 2 7 41
# 2 8 84
# 2 12 16
# 2 15 45
# 2 17 77
# 2 18 82
# 3 4 34
# 3 5 89
# 3 8 58
# 3 11 71
# 3 14 79
# 3 15 96
# 4 6 18
# 4 7 57
# 4 9 87
# 4 10 94
# 4 11 57
# 4 13 69
# 4 14 23
# 4 18 38
# 4 19 26
# 5 10 23
# 5 19 67
# 6 9 46
# 6 15 33
# 7 17 48
# 7 18 59
# 8 10 34
# 8 12 78
# 8 15 36
# 8 16 51
# 9 11 17
# 9 13 74
# 9 18 63
# 9 19 71
# 10 12 31
# 11 12 73
# 11 13 31
# 11 16 25
# 11 19 90
# 12 13 47
# 12 18 17
# 12 19 10
# 13 14 56
# 13 18 84
# 14 16 81
# 14 19 60
# 15 19 50
# 16 19 1
# 13 1

#salida3
# 104
# 13 12 19 1