def solve(data):
    #ordenamos actividades en función de cuando acaben
    actividades = sorted(data['actividades'], key=lambda x: x['F'])

    #inicializamos variables
    max_actividades = 0
    fin_ultima = 0

    #recorremos las actividades
    for actividad in actividades:
        #si la actividad empieza después de que acabe la última, la añadimos
        if actividad['I'] >= fin_ultima:
            max_actividades += 1
            fin_ultima = actividad['F']
    print(max_actividades)


N = int(input())  # Leer la cantidad de famosos
actividades = []

# Leer los datos de cada famoso línea por línea
for _ in range(N):
    entrada = input().split()  # Leer una línea y dividirla en partes
    A = entrada[0]    # Nombre de la actividad
    I = int(entrada[1])  # Valor Inicio
    F = int(entrada[2])  # Valor Fin
    actividades.append({'A': A, 'I': I, 'F': F})

# Agrupamos en data
data = {'N': N, 'actividades': actividades}

solve(data)

#Entrada 1
# 5
# Vacunarse 20 30
# BaniarAlPez 35 40
# Entrenar 31 60
# PonerTweets 10 15
# LlamadaConIbai 80 100

#Salida 1
#4

#Entrada 2
# 9
# BXRDMVSDEF 556 7139
# UXJUGYEDIM 8378 9352
# MIPQVDUKJU 7653 8874
# YUQPNHMHHO 4144 5256
# YVBLMXMCAW 3197 5183
# IAUCAQNEYL 798 3918
# LROTLCJSPO 5668 7227
# HKLJCJXSLE 1299 6782
# UGHWUPWJPV 2908 7481

#Salida 2
#4
