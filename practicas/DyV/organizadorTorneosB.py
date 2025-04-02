import sys

"""
Problema: Organizador de Torneos
Descripción: Se requiere contar el número de inversiones en una lista de puntuaciones de un torneo. 
Una inversión se define como un par (i, j) tal que i < j y arr[i] > arr[j].
"""
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Índice para la primera mitad
    j = mid + 1 # Índice para la segunda mitad
    k = left    # Índice para la combinación ordenada
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Contar inversiones
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


"""
Función principal para contar inversiones usando Merge Sort
"""
def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count

"""
Función para resolver el problema, recibiendo un diccionario con los datos
"""
def solve(data):
    arr = data['scores']
    n = len(arr)
    temp_arr = [0] * n
    result = merge_sort_and_count(arr, temp_arr, 0, n - 1)
    print(result)

def main():
    N = int(sys.stdin.readline().strip())
    scores = list(map(int, sys.stdin.readline().split()))
    data = {'scores': scores}
    solve(data)

if __name__ == "__main__":
    main()

# entrada 1
# 4
# 4 3 2 1

# salida 1
# 6