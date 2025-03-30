def solve(data):
    # Creamos el mapeo para las cualidades con las claves correctas
    cualidades = {"beauty": 'b', "intelligence": 'i', "kindness": 'k'}
    clave = cualidades[data['caracteristica']]  # Extraemos la clave correspondiente

    # Ordenamos las parejas según el beneficio por tiempo de forma descendente
    parejas = sorted(data['parejas'], key=lambda x: (-x[clave] / x['t'], -x[clave]))

    # Inicializamos las variables
    seleccionados = []
    beneficio = 0.0
    tiempo_restante = data['tiempo_maximo']

    # Recorremos las parejas seleccionadas
    for pareja in parejas:
        nombre = pareja['nombre']
        valor = pareja[clave]
        tiempo = pareja['t']

        if tiempo_restante >= tiempo:
            seleccionados.append(nombre)
            beneficio += valor
            tiempo_restante -= tiempo
        else:
            beneficio += (valor * tiempo_restante) / tiempo  # Si no hay suficiente tiempo
            seleccionados.append(nombre)
            break

    # Mostramos los resultados
    print(' '.join(seleccionados))
    print("{:.2f}".format(beneficio))
    print()


N = int(input())  # Número de concursantes

for _ in range(N):
    caracteristica = input().strip()  # Cualidad que más valora el concursante
    tiempo_maximo = int(input())  # Tiempo máximo que tiene el concursante
    T = int(input())  # Número de parejas posibles

    parejas = []  # Lista para almacenar las parejas disponibles

    # Recogemos la información de las parejas
    for i in range(T):
        datos_pareja = input().split()
        nombre = datos_pareja[0]
        belleza = int(datos_pareja[1])
        inteligencia = int(datos_pareja[2])
        amabilidad = int(datos_pareja[3])
        tiempo = int(datos_pareja[4])

        pareja = {
            'nombre': nombre,
            'b': belleza,
            'i': inteligencia,
            'k': amabilidad,
            't': tiempo
        }
        parejas.append(pareja)

    # Creamos el diccionario con la información del concursante
    data = {
        'tiempo_maximo': tiempo_maximo,
        'caracteristica': caracteristica,
        'parejas': parejas
    }

    solve(data)

#entrada 1
# 2
# intelligence
# 625
# 10
# DonBarrett 67 4 69 30
# WarrenHaris 91 46 86 24
# KeithFurstenberg 98 57 64 53
# JulioReed 87 63 30 37
# LeeMinton 35 72 45 8
# ChuckMoore 94 11 61 8
# JonathanParker 31 13 100 57
# ShawnLuhnow 46 51 73 4
# JackieDarrah 35 42 57 40
# DavidRomero 14 48 67 31
# beauty
# 525
# 10
# JamesLee 55 21 12 50
# JasonHalman 4 81 27 11
# DustinFrye 20 40 67 5
# HenryHooks 58 9 50 59
# JoelWhite 64 57 53 11
# JesseHumphrey 41 44 86 73
# DouglasKurtz 25 92 34 9
# LarryReid 20 3 33 62
# RobertAustin 40 87 17 63
# JamesEvans 77 85 88 12

#salida1
# ShawnLuhnow LeeMinton WarrenHaris JulioReed DavidRomero ChuckMoore KeithFurstenberg JackieDarrah JonathanParker DonBarrett
# 407.00
# JamesEvans JoelWhite DustinFrye DouglasKurtz JamesLee HenryHooks RobertAustin JesseHumphrey JasonHalman LarryReid
# 404.00

#entrada 2
# 5
# kindness
# 506
# 10
# JayBird 9 97 96 32
# JohnGaietto 37 28 33 86
# CarlVasquez 23 89 93 11
# MichaelSampson 36 89 37 76
# ThomasPelletier 90 10 14 46
# CharlesRomero 78 60 39 94
# RaymondElam 80 63 74 95
# MichaelStinnett 30 24 7 2
# MarvinCampbell 5 22 56 54
# JoshuaRoyal 26 39 78 17
# intelligence
# 650
# 10
# BillWard 92 24 23 81
# RonPalmer 29 60 61 33
# DavidMcnair 80 75 40 88
# StevenDingle 97 73 45 44
# RalphHenry 81 16 8 98
# RonaldFeurtado 93 34 29 24
# PatrickHawley 38 62 35 63
# WilliamPeters 73 2 10 48
# MichaelSmith 44 18 48 35
# MarkBogart 36 83 53 47
# beauty
# 600
# 10
# OscarStribling 62 51 35 92
# MatthewAdams 65 85 2 21
# JonathanSpeigel 11 57 41 46
# DavidTyson 82 95 2 2
# MarkMunoz 13 29 71 2
# RandyMona 72 50 57 13
# WilliePepper 97 7 94 27
# DavidSnider 72 24 68 41
# DavidWestendorf 38 15 95 24
# ToddFinley 61 99 31 84
# kindness
# 512
# 10
# GeorgeEvans 77 31 78 65
# AndrewObrien 68 54 35 79
# EricHenley 80 26 61 74
# DanielAlexander 80 29 94 98
# JessieSchmidt 15 46 67 26
# JosephAustin 78 93 61 84
# MaxHallum 3 27 18 79
# JoshuaFrost 30 41 91 26
# LonnieNorrell 39 31 22 93
# DennyCyrus 9 86 57 51
# intelligence
# 660
# 10
# TravisCooke 81 47 35 17
# JoeCastellanos 63 5 47 50
# QuintonJefferson 78 36 40 100
# AlexHolt 98 60 74 96
# MorrisBurke 73 28 64 51
# CharlesBolden 5 10 39 12
# WilliamBrown 66 60 52 23
# GeorgeFarrish 34 89 29 12
# GregoryAdams 86 28 23 92
# RogerLozey 12 30 23 4

#salida 2
# CarlVasquez JoshuaRoyal MichaelStinnett JayBird MarvinCampbell RaymondElam MichaelSampson CharlesRomero JohnGaietto ThomasPelletier
# 524.87
# RonPalmer MarkBogart StevenDingle RonaldFeurtado PatrickHawley DavidMcnair MichaelSmith BillWard RalphHenry WilliamPeters
# 447.00
# DavidTyson MarkMunoz RandyMona WilliePepper MatthewAdams DavidSnider DavidWestendorf ToddFinley OscarStribling JonathanSpeigel
# 573.00
# JoshuaFrost JessieSchmidt GeorgeEvans DennyCyrus DanielAlexander EricHenley JosephAustin AndrewObrien LonnieNorrell
# 546.13
# RogerLozey GeorgeFarrish TravisCooke WilliamBrown CharlesBolden AlexHolt MorrisBurke QuintonJefferson GregoryAdams JoeCastellanos
# 393.00

#entrada3
# 7
# beauty
# 629
# 10
# JeffreyGerber 15 23 85 43
# ShaneWelch 30 90 65 63
# LeonardSmith 34 52 14 44
# DannyColeman 42 15 92 73
# AndrewLynn 73 80 22 1
# JamesVelez 60 14 71 37
# DouglasSantiago 91 48 83 17
# AlanLuna 69 21 99 38
# PatrickDevalk 6 51 50 20
# SalvadorKunst 24 43 48 22
# kindness
# 645
# 10
# DanielLopez 67 43 28 87
# JamesRoberts 60 9 91 38
# WesleyReiber 100 72 23 18
# LeonardWilliams 69 64 38 76
# DannyBeasley 50 63 21 41
# GuadalupeHand 67 92 65 64
# LarryWales 40 61 8 64
# JohnSchrum 83 90 38 78
# WilliamSimien 76 61 56 59
# KennethBurks 88 24 72 12
# beauty
# 588
# 10
# JamesMorris 71 97 17 11
# JoeBenson 98 30 67 99
# JonathanPena 57 4 53 73
# SteveHill 7 13 28 19
# TravisMartinez 99 46 70 92
# DavidFontaine 70 83 44 52
# SaulDietrick 58 38 53 88
# ClaytonMorrow 61 94 57 32
# RomanRobinson 31 34 23 37
# AltonMynatt 98 71 85 96
# kindness
# 592
# 10
# JoshuaPowell 25 70 65 94
# JoseMyers 11 29 55 66
# RobertOrr 16 52 45 57
# WilbertWright 36 58 65 26
# RobertLong 93 66 74 91
# OtisVelasquez 72 74 26 28
# JesseFlanagan 56 72 1 32
# HowardTello 23 54 33 44
# DavidHampton 14 35 66 16
# HollisBica 64 75 46 98
# beauty
# 529
# 10
# AnthonyCuchares 92 13 90 6
# EarnestMays 26 98 14 90
# OscarServant 56 22 42 52
# AnthonyGaston 45 31 15 93
# DavidSchwartz 60 75 55 62
# RusselWilliams 80 97 34 46
# DavidThomsen 81 49 60 41
# HomerWoodmansee 5 47 48 91
# RichardFlaherty 6 38 87 71
# ShawnStout 68 87 93 2
# intelligence
# 552
# 10
# ChristopherRiley 24 28 14 43
# DonaldMerrill 79 27 45 21
# JamesFine 78 57 80 3
# MatthewPittsley 7 39 87 58
# RobertRocha 68 12 47 57
# JeremiahBurris 70 53 78 61
# RalphOrozco 47 100 18 94
# DavidSamuel 64 41 50 53
# LannyHuffman 84 57 8 90
# EarlWilson 95 41 61 30
# intelligence
# 567
# 10
# BryonLackey 84 76 68 75
# AlShaner 61 30 11 66
# RandyFurman 69 72 76 100
# ArthurMann 3 59 86 22
# JesseMendez 22 70 2 80
# DonaldHaskett 87 96 64 15
# EveretteEgan 24 79 34 59
# StevenBoyle 80 83 57 12
# RobertSmith 5 24 33 76
# CurtisTomassi 49 1 97 29

#salida 3
# AndrewLynn DouglasSantiago AlanLuna JamesVelez SalvadorKunst LeonardSmith DannyColeman ShaneWelch JeffreyGerber PatrickDevalk
# 444.00
# KennethBurks JamesRoberts WesleyReiber GuadalupeHand WilliamSimien DannyBeasley LeonardWilliams JohnSchrum DanielLopez LarryWales
# 440.00
# JamesMorris ClaytonMorrow DavidFontaine TravisMartinez AltonMynatt JoeBenson RomanRobinson JonathanPena SaulDietrick SteveHill
# 645.95
# DavidHampton WilbertWright OtisVelasquez JoseMyers RobertLong RobertOrr HowardTello JoshuaPowell HollisBica JesseFlanagan
# 476.00
# ShawnStout AnthonyCuchares DavidThomsen RusselWilliams OscarServant DavidSchwartz AnthonyGaston EarnestMays RichardFlaherty HomerWoodmansee
# 517.63
# JamesFine EarlWilson DonaldMerrill RalphOrozco JeremiahBurris DavidSamuel MatthewPittsley ChristopherRiley LannyHuffman RobertRocha
# 455.00
# StevenBoyle DonaldHaskett ArthurMann EveretteEgan BryonLackey JesseMendez RandyFurman AlShaner RobertSmith CurtisTomassi
# 590.00


