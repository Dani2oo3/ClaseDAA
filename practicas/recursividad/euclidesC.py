def mcmRecursivo(a, b):
    if b == 0:
        return a
    else:
        return mcmRecursivo(b, a % b)

data = input().split()
a = int(data[0])
b = int(data[1])

print(mcmRecursivo(a, b))

#entrada1
# 48 18

#salida1
# 6

#entrada2
# 47 67

#salida2
# 1

#entrada3
# 60 26

#salida3
# 2
