def solve(data):
    # Ordenar los participantes por edad de manera ascendente
    data['participantes'].sort(key=lambda x: x['edad'])

    # Dividir en dos grupos óptimos directamente
    grupo_jovenes = data['participantes'][:2]
    grupo_no_tan_jovenes = data['participantes'][2:]

    # Imprimir los grupos en el orden correcto
    print(" ".join(p['nombre'] for p in grupo_jovenes))
    print(" ".join(p['nombre'] for p in grupo_no_tan_jovenes))

# Leer N y K
N, K = map(int, input().split())
participantes = []

# Leer los datos de cada participante
for _ in range(N):
    entrada = input().split()
    nombre = entrada[0]
    edad = int(entrada[1])
    participantes.append({'nombre': nombre, 'edad': edad})

# Agrupar en data
data = {'N': N, 'K': K, 'participantes': participantes}

solve(data)

#entrada1
# 5 2
# JamesLineberger 55
# JeanetteMaurey 73
# ChristieDangelo 29
# HeatherTrew 78
# LeolaSwift 30

#salida1
# ChristieDangelo LeolaSwift
# JamesLineberger JeanetteMaurey HeatherTrew

#entrada2
# 5 3
# TammyEvans 67
# TimothyLeflore 96
# LaurenHumphrey 37
# DonnyLopez 93
# LorettaFox 36

#salida2
# LorettaFox LaurenHumphrey
# TammyEvans DonnyLopez TimothyLeflore
