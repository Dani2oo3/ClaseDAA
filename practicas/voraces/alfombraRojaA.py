# data de entrada
# 5                          N --> Numero de famosos esperando
# Rivers 80 50 6             S --> Nombre del famoso,
# Ibai 65 60 7               M --> Amabilidad,
# KanyeWest 10 2 1           L --> fama,
# TaylorSwift 90 95 10       T --> tiempo entrevistado.
# Chiara 85 20 4

def solve(data):
    #Variables
    tiempo = 0
    seguirSumando = True

    # Ordenamos alfabeticamente y vemos quien es el primero
    data['famosos'].sort(key=lambda x: x['S']) # O(n log n)
    primero = data['famosos'][0]['S']

    #Ordenamos según (Fama / Amabilidad) y vemos quien es el primero
    data['famosos'].sort(key=lambda x: (-x['L'] / x['M'], x['S']))  # O(n log n)

    # pintamos el nombre de los famosos
    for personas in data['famosos']:
        print(personas['S'])
        if seguirSumando and personas['S'] != primero:
            tiempo += personas['T']
        else:
            seguirSumando = False
    print(tiempo)

N = int(input())  # Leer la cantidad de famosos
famosos = []

# Leer los datos de cada famoso línea por línea
for _ in range(N):
    entrada = input().split()  # Leer una línea y dividirla en partes
    S = entrada[0]    # Nombre del famoso
    M = int(entrada[1])  # Valor M
    L = int(entrada[2])  # Valor L
    T = int(entrada[3])  # Valor T
    famosos.append({'S': S, 'M': M, 'L': L, 'T': T})

# Estructurar los datos
data = {'N': N, 'famosos': famosos}

solve(data)  # Llamar a la función solve con el diccionario data

# Entrada 1
# 4
# Juan 25 10 6
# Sergio 40 60 7
# Elena 35 12 9
# Hector 12 34 1

# Salida 1
#Hector
# Sergio
# Juan
# Elena
# 14

# Entrada 2
# 5
# Rivers 80 50 6
# Ibai 65 60 7
# KanyeWest 10 2 1
# TaylorSwift 90 95 10
# Chiara 85 20 4

# Salida 2
# TaylorSwift
# Ibai
# Rivers
# Chiara
# KanyeWest
# 23

# Entrada 3
# 5
# Marco 4 3 2
# Irene 10 2 3
# Antonio 6 9 1
# Claudia 2 7 4
# Maria 9 8 2

# Salida 3
# Claudia
# Antonio
# Maria
# Marco
# Irene
# 4
