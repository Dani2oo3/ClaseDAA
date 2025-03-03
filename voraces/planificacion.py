def getBestItem(data, candidates):
    bestProfit = 0
    bestItem = 0
    for c in candidates:
        profit = data['profit'][c]
        if profit > bestProfit:
            bestProfit = data['profit'][c]
            bestItem = c
    return bestItem

def isFeaseable(schedule, i):
    return schedule[i] == -1

def solve(data):
    n = len(data['profit'])
    candidates = set()

    for i in range(n):
        candidates.add(i)
    Ndays = max(data['deadline'])
    schedule = [-1] * (Ndays + 1)

    while candidates:
        bestCandidate = getBestItem(data, candidates)
        candidates.remove(bestCandidate)
        i = data['deadline'][bestCandidate]

        found = False  # Inicializamos found antes de usarlo
        while i >= 1 and not found:
            if isFeaseable(schedule, i):
                schedule[i] = bestCandidate
                found = True
            i -= 1
    return schedule

def printSol(data, schedule):
    print("Task\tProfit\tDateOriginal\tDeadLine")
    totalProfit = 0
    for i in range(len(schedule)):
        task = schedule[i]
        if task != -1:  # Corregido
            print(str(task) + '\t\t' + str(data['profit'][task]) + '\t\t' + str(i) + '\t\t' + str(data['deadline'][task]))
            totalProfit += data['profit'][task]
    print("PROFIT: " + str(totalProfit))

# inicializacion de variables

data = {
    'profit': [50, 10, 15, 30],
    'deadline': [2, 1, 2, 1]
}

schedule = solve(data)
print(schedule)
printSol(data, schedule)