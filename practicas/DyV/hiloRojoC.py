import sys

"""Realiza búsqueda binaria en arr para encontrar la posición de x."""
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

"""
Resuelve el problema de encontrar posiciones en dos grupos de números.
"""
def solve(data):
    group1, group2, connections = data['group1'], data['group2'], data['connections']
    pos1 = {value: idx for idx, value in enumerate(group1)}
    pos2 = {value: idx for idx, value in enumerate(group2)}

    for a, b in connections:
        if a in pos1 and b in pos2:
            print(pos1[a], pos2[b])
        else:
            print("SIN DESTINO")


def main():
    N = int(sys.stdin.readline().strip())
    group1 = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    group2 = list(map(int, sys.stdin.readline().split()))
    P = int(sys.stdin.readline().strip())
    connections = [tuple(map(int, sys.stdin.readline().split())) for _ in range(P)]

    data = {'group1': group1, 'group2': group2, 'connections': connections}
    solve(data)


if __name__ == "__main__":
    main()

# entrada 1
# 6
# 5 21 32 42 87 92
# 4
# 10 50 78 97
# 3
# 87 97
# 21 10
# 32 40

# salida 1
# 4 3
# 1 0
# SIN DESTINO

# entrada 2
# 10
# 37036 119991 227138 327291 332258 381774 479553 480061 637012 852699
# 10
# 38560 136237 173057 197161 359481 516138 565549 700896 743348 857364
# 59
# 119991 857364
# 227138 700896
# 37036 173057
# 119991 516138
# 852699 565549
# 332258 38560
# 332258 38560
# 1597507 1900986
# 332258 565549
# 327291 1837826
# 480061 38560
# 37036 857364
# 480061 173057
# 1579808 516138
# 227138 857364
# 227138 1867911
# 1254568 1419599
# 332258 359481
# 852699 857364
# 332258 38560
# 479553 197161
# 119991 565549
# 1250215 197161
# 381774 743348
# 1572265 136237
# 37036 857364
# 1970094 1139482
# 852699 1850541
# 479553 743348
# 637012 565549
# 1075644 38560
# 1619644 38560
# 1577770 857364
# 37036 173057
# 381774 1036294
# 332258 700896
# 327291 38560
# 1217878 700896
# 327291 857364
# 1439887 136237
# 381774 743348
# 332258 38560
# 227138 565549
# 327291 516138
# 1538952 516138
# 332258 359481
# 37036 136237
# 327291 565549
# 637012 197161
# 1199467 38560
# 480061 565549
# 479553 857364
# 479553 197161
# 1109265 359481
# 479553 359481
# 479553 38560
# 480061 516138
# 637012 197161
# 227138 700896

# salida 2
# 1 9
# 2 7
# 0 2
# 1 5
# 9 6
# 4 0
# 4 0
# SIN DESTINO
# 4 6
# SIN DESTINO
# 7 0
# 0 9
# 7 2
# SIN DESTINO
# 2 9
# SIN DESTINO
# SIN DESTINO
# 4 4
# 9 9
# 4 0
# 6 3
# 1 6
# SIN DESTINO
# 5 8
# SIN DESTINO
# 0 9
# SIN DESTINO
# SIN DESTINO
# 6 8
# 8 6
# SIN DESTINO
# SIN DESTINO
# SIN DESTINO
# 0 2
# SIN DESTINO
# 4 7
# 3 0
# SIN DESTINO
# 3 9
# SIN DESTINO
# 5 8
# 4 0
# 2 6
# 3 5
# SIN DESTINO
# 4 4
# 0 1
# 3 6
# 8 3
# SIN DESTINO
# 7 6
# 6 9
# 6 3
# SIN DESTINO
# 6 4
# 6 0
# 7 5
# 8 3
# 2 7
