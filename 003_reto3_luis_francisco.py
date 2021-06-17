# Aplicar la estrategia divide y venceras

# Primero se requiere obtener información del número de zonas
# Ingresar el número de zonas
zonas = int(input())

# Segundo se requiere calcular el promedio de cada zona
# para la materia organica y el oxido de fosforo
promedio_materia_organica = []
promedio_oxido_fosforo = []
for i in range(0, zonas, 1):
    # En esta parte se utiliza lo señalado en
    # https://www.w3schools.com/python/ref_string_split.asp
    # Ingresar los valores de la zona {i + 1} de materia organica
    materia_organica = input().split(" ")
    # En esta parte se utiliza lo señalado en
    # https://www.w3schools.com/python/ref_string_split.asp
    # Ingresar los valores de la zona {i + 1} de oxido de fosforo
    oxido_fosforo = input().split(" ")
    # Luego debemos convertir cada elemento de las listas
    # de caracteres a tipo float
    for i in range(0, len(materia_organica), 1):
        materia_organica[i] = float(materia_organica[i])
        oxido_fosforo[i] = float(oxido_fosforo[i])
    # Luego debemos calcular el promedio de cada zona y empezar
    # a guardar cada resultado
    promedio_materia_organica.append(
        sum(materia_organica) / len(materia_organica))
    promedio_oxido_fosforo.append(
        sum(oxido_fosforo) / len(oxido_fosforo))

# Tercero se requiere realizar el conteo de cada
# categoria en base a los promedios de la
# materia orgánica y el oxido de fósforo
n_sumamente_apto = 0
n_moderadamente_apto = 0
n_marginalmente_apto = 0
n_no_apto = 0
for i in range(0, len(promedio_materia_organica), 1):
    # sumamente apto
    if (promedio_materia_organica[i] > 5 and promedio_oxido_fosforo[i] > 69):
        n_sumamente_apto = n_sumamente_apto + 1

    # moderadamente apto
    elif (promedio_materia_organica[i] > 4 and promedio_oxido_fosforo[i] > 57):
        n_moderadamente_apto = n_moderadamente_apto + 1

    # marginalmente apto
    elif (promedio_materia_organica[i] >= 3 and promedio_oxido_fosforo[i] >= 46):
        n_marginalmente_apto = n_marginalmente_apto + 1

    # no apto
    else:
        n_no_apto = n_no_apto + 1

# Cuarto se realiza la impresión de los resultados
# en base al formato solicitado
for i in range(0, len(promedio_materia_organica), 1):
    if i != len(promedio_materia_organica) - 1:
        print(f"{promedio_materia_organica[i]:.2f}", end=" ")
    else:
        print(f"{promedio_materia_organica[i]:.2f}", end="\n")

for i in range(0, len(promedio_materia_organica), 1):
    if i != len(promedio_materia_organica) - 1:
        print(f"{promedio_oxido_fosforo[i]:.2f}", end=" ")
    else:
        print(f"{promedio_oxido_fosforo[i]:.2f}", end="\n")

print(f"sumamente apto {n_sumamente_apto}")
print(f"moderadamente apto {n_moderadamente_apto}")
print(f"marginalmente apto {n_marginalmente_apto}")
print(f"no apto {n_no_apto}")

# Valores de prueba

# 3
# 4.84 4.8 6.05 4.84 4.85
# 49 72 48 78 74
# 4.36 2.62 5.24 5.42 4.43
# 76 41 63 53 75
# 3.43 3.51 4.31 3.67 5.25
# 71 61 46 67 45

# 3
# 5.64 3.82 5.3 6.16 5.02 6.17 3.22 2.55 5.5 5.0
# 73 69 71 55 45 70 68 46 63 44
# 4.49 2.77 4.82 2.76 3.51 4.05 4.42 6.08 3.93 4.81
# 67 56 56 43 50 78 67 75 75 42
# 2.6 4.63 3.95 2.92 3.77 3.11 4.28 3.77 4.92 3.66
# 73 58 71 70 54 59 78 66 50 76
