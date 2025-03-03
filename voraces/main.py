"""
data[claves]
    profit: lista de beneficios
    weight: lista de pesos
    W: peso máximo

    data[key] = [weight]
    data[key][i-esimo]

    key = {weight, profit}
    data['profit'] = [1, 2, 3, 4, 5, 6]
"""

def isFeaseable(data, bestCandidate, W):
    return data['weight'][bestCandidate] <= W

def getBestItem(candidates, data):
    bestRatio = -1 # No hay ningun objeto seleccionado
    bestItem = -1 # No hay ningun objeto seleccionado

    for c in candidates: #1 [0, 1, 2, 3, 4, 5] - 2 [0, 1, 3, 4, 5]
        ratio = data['profit'][c] / data['weight'][c]
        if ratio > bestRatio:
            bestRatio = ratio
            bestItem = c
    return bestItem

def solve(data):
    numObjetos = len(data['profit'])
    candidates = set()

    for i in range(numObjetos):
        candidates.add(i)

    x = [0.0] * numObjetos # No hay ningun objeto seleccionado
    W = data['W']
    isSol = False

    while not isSol and candidates:
        bestCandidate = getBestItem(candidates, data)
        candidates.remove(bestCandidate)

        if isFeaseable(data, bestCandidate, W):
            x[bestCandidate] = 1.0
            W -= data['weight'][bestCandidate]
        else: # Debemos fraccionar
            isSol = True
            x[bestCandidate] = W / data['weight'][bestCandidate]
            W = 0
    return x

# inicializacion de variables

data = {}
data['profit'] = [20, 30, 66, 40, 60]
data['weight'] = [10, 20, 30, 40, 50]
data['W'] = 100

x = solve(data)
print(x)