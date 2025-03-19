def reverso(data):
    if len(data) == 0:
        return ''
    else:
        return data[-1] + reverso(data[:-1])

data = input()
print(reverso(data))

#entrada1
# dog

#salida1
# god

#entrada2
# alucard

#salida2
# dracula