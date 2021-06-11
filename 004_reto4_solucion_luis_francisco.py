# Aplicar la estrategia divide y venceras

# Primero se requiere obtener información del número de zonas
# Ingresar el número de zonas
zonas = int(input())

# Segundo se requiere guardar los datos en una matriz
# de la variable materia orgánica
matriz_materia_organica = []
for i in range(0, zonas, 1):
    # En esta parte se utiliza lo señalado en
    # https://www.w3schools.com/python/ref_string_split.asp
    # Ingresar los valores de la zona {i + 1} de materia organica
    materia_organica = input().split(" ")
    fila_materia_organica = []
    # Luego debemos convertir cada elemento de la lista
    # de caracteres a tipo float
    for i in range(0, len(materia_organica), 1):
        fila_materia_organica.append(float(materia_organica[i]))
    # Luego debemos agregar la fila a la matriz
    matriz_materia_organica.append(fila_materia_organica)

# Tercero se requiere guardar los datos en una matriz
# de la variable óxido de fosforo
matriz_oxido_fosforo = []
for i in range(0, zonas, 1):
    # En esta parte se utiliza lo señalado en
    # https://www.w3schools.com/python/ref_string_split.asp
    # Ingresar los valores de la zona {i + 1} de materia organica
    oxido_fosforo = input().split(" ")
    fila_oxido_fosforo = []
    # Luego debemos convertir cada elemento de la lista
    # de caracteres a tipo float
    for i in range(0, len(materia_organica), 1):
        fila_oxido_fosforo.append(float(oxido_fosforo[i]))
    # Luego debemos agregar la fila a la matriz
    matriz_oxido_fosforo.append(fila_oxido_fosforo)

# Cuarto se requiere realizar el conteo de cada
# categoria para cada zona en base a la información
# de las matrices matriz_materia_organica y
# matriz_oxido_fosforo
# Para realizar este proceso y mantener los datos
# consolidados se construye una matriz donde las
# columnas corresponden a las categorias (no_apto,
# marginalmente_apto, moderadamente_apto, sumamente_apto)
# y las filas a cada zona
matriz_categorias_zonas = []
for i in range(0, len(matriz_materia_organica), 1):
    # Fijar las varibles de conteo
    n_sumamente_apto = 0
    n_moderadamente_apto = 0
    n_marginalmente_apto = 0
    n_no_apto = 0
    # Generar el conteo para cada zona
    for j in range(0, len(matriz_materia_organica[0]), 1):
        # sumamente apto
        if (matriz_materia_organica[i][j] > 5 and matriz_oxido_fosforo[i][j] > 69):
            n_sumamente_apto = n_sumamente_apto + 1

        # moderadamente apto
        elif (matriz_materia_organica[i][j] > 4 and matriz_oxido_fosforo[i][j] > 57):
            n_moderadamente_apto = n_moderadamente_apto + 1

        # marginalmente apto
        elif (matriz_materia_organica[i][j] >= 3 and matriz_oxido_fosforo[i][j] >= 46):
            n_marginalmente_apto = n_marginalmente_apto + 1

        # no apto
        else:
            n_no_apto = n_no_apto + 1

    # Guardar el conteo por categorias para cada zona
    matriz_categorias_zonas.append(
        [n_no_apto, n_marginalmente_apto, n_moderadamente_apto, n_sumamente_apto])

# Quinto se realiza el conteo de cada categoria
# (no_apto, marginalmente_apto, moderadamente_apto,
# sumamente_apto)
conteo_categorias = []
for j in range(0, len(matriz_categorias_zonas[0]), 1):
    suma = 0
    for i in range(0, len(matriz_categorias_zonas), 1):
        suma = suma + matriz_categorias_zonas[i][j]
    conteo_categorias.append(suma)

# Sexto se selecciona la categoría que más se
# presenta por zona donde si existe un empate
# se escoje la mejor categoría
categoria_mas_se_presenta = []
for i in range(0, len(matriz_categorias_zonas), 1):
    # Especificar el máximo
    maximo = max(matriz_categorias_zonas[i])
    # sumamente apto
    if matriz_categorias_zonas[i][3] == maximo:
        categoria_mas_se_presenta.append("sumamente apto")
    # moderadamente apto
    elif matriz_categorias_zonas[i][2] == maximo:
        categoria_mas_se_presenta.append("moderadamente apto")
    # marginalmente apto
    elif matriz_categorias_zonas[i][1] == maximo:
        categoria_mas_se_presenta.append("marginalmente apto")
    # no apto
    else:
        categoria_mas_se_presenta.append("no apto")

# Septimo se selecciona la categoría que menos se
# presenta por zona donde si existe un empate
# se escoje la mejor categoría
# Además si no se presenta una categoría, no debe
# ser tenida en cuenta. Es decir, si el conteo por zona
# de una categoria es cero, esa categoría no será considerada
# como la que menos se presentó.

# Septimo a: Construimos una función auxiliar que encuentre el
# segundo elemento más pequeño. Para el caso del reto4 esta función
# no tendrá problemas dado que el segundo elemento más pequeño
# siempre existe


def segundo_min(lista):
    minimo = min(lista)
    segundo_min = lista[0]
    for i in range(0, len(lista), 1):
        # Esta parte se incluye dado que
        # el mínimo podría estar en una
        # posición anterior a cualquier otro
        # número y la parte del elif no
        # funcionaría. Por ejemplo [1,5] o [1,1,5]
        if minimo == segundo_min:
            segundo_min = lista[i+1]
        elif minimo < lista[i] and segundo_min > lista[i]:
            segundo_min = lista[i]
    return segundo_min


# Septimo b: se selecciona la categoría que menos se
# presenta por zona donde si existe un empate
# se escoje la mejor categoría y se tiene en cuenta el
# caso cuando el mínimo es cero

categoria_menos_se_presenta = []
for i in range(0, len(matriz_categorias_zonas), 1):

    # Calcular el mínimo
    minimo = min(matriz_categorias_zonas[i])

    # Caso en el que el mínimo sea diferente de cero
    if minimo != 0:

        # sumamente apto
        if matriz_categorias_zonas[i][3] == minimo:
            categoria_menos_se_presenta.append("sumamente apto")
        # moderadamente apto
        elif matriz_categorias_zonas[i][2] == minimo:
            categoria_menos_se_presenta.append("moderadamente apto")
        # marginalmente apto
        elif matriz_categorias_zonas[i][1] == minimo:
            categoria_menos_se_presenta.append("marginalmente apto")
        # no apto
        else:
            categoria_menos_se_presenta.append("no apto")

    # Caso en el que el mínimo sea igual a cero
    else:
        # Calcular el segundo elemento más pequeño
        segundo_minimo = segundo_min(matriz_categorias_zonas[i])

        # sumamente apto
        if matriz_categorias_zonas[i][3] == segundo_minimo:
            categoria_menos_se_presenta.append("sumamente apto")
        # moderadamente apto
        elif matriz_categorias_zonas[i][2] == segundo_minimo:
            categoria_menos_se_presenta.append("moderadamente apto")
        # marginalmente apto
        elif matriz_categorias_zonas[i][1] == segundo_minimo:
            categoria_menos_se_presenta.append("marginalmente apto")
        # no apto
        else:
            categoria_menos_se_presenta.append("no apto")

# Octavo se realiza la impresión de los resultados
# en base al formato solicitado

# Conteo de categorias
for i in range(0, len(conteo_categorias), 1):
    if i != len(conteo_categorias) - 1:
        print(f"{conteo_categorias[i]}", end=" ")
    else:
        print(f"{conteo_categorias[i]}", end="\n")

# Categorias que mas se presentan
for i in range(0, len(categoria_mas_se_presenta), 1):
    if i != len(categoria_mas_se_presenta) - 1:
        print(f"{categoria_mas_se_presenta[i]}", end=",")
    else:
        print(f"{categoria_mas_se_presenta[i]}", end="\n")

# Categorias que menos se presentan
for i in range(0, len(categoria_menos_se_presenta), 1):
    if i != len(categoria_menos_se_presenta) - 1:
        print(f"{categoria_menos_se_presenta[i]}", end=",")
    else:
        print(f"{categoria_menos_se_presenta[i]}", end="\n")

# Valores de prueba

# 3
# 5.62 2.33 1.97 4.78 4.21 1.64 4.26
# 2.09 7.12 7.13 3.62 1.87 4.11 2.14
# 5.09 3.19 5.17 4.5 4.99 3.21 5.24
# 63 58 42 64 46 45 62
# 72 42 53 77 77 43 56
# 59 56 58 67 48 79 49
