# Primero, escoger una ciudad
# No se incluyen mensajes en los inputs
ciudad = input()

# Segundo, abrir el archivo
archivo = open("data.csv", mode='r', encoding='UTF-8')

# Tercero, leer el archivo linea por linea
# hasta que se vacie

# En esta parte se define fila para incluirla
# en el while y también para no incluir la
# primera fila donde se encuentran los nombres
# de las variables
fila = archivo.readline()

capital = []
materia_organica = []
p2o5 = []
aptitud = []

while fila:
    # Definir la fila separandola en una lista y
    # eliminando el salto de línea
    fila = archivo.readline()
    # Es necesario eliminar la última linea que contiene
    # ''
    if fila != '':
        # En esta parte se utilizó lo señalado en
        # https://www.w3schools.com/python/python_ref_string.asp
        data_lista = fila.rstrip('\n').split(',')
        # Generar listas con las variables de interes
        capital.append(data_lista[0])
        materia_organica.append(data_lista[3])
        p2o5.append(data_lista[4])
        aptitud.append(data_lista[6])

# Cuarto, identificar las posiciones donde se encuentra
# la ciudad seleccionada
posicion = []
for i in range(0, len(capital), 1):
    if capital[i] == ciudad:
        posicion.append(i)

# Quinto, filtrar las variables de interés
# asociadas con la ciudad seleccionada
ciudad_materia_organica = []
ciudad_p2o5 = []
ciudad_aptitud = []
for i in posicion:
    ciudad_materia_organica.append(float(materia_organica[i]))
    ciudad_p2o5.append(float(p2o5[i]))
    ciudad_aptitud.append(aptitud[i])

# Sexto, calcular los promedios de las variables
# materia_organica y p2o5
promedio_materia_organica_p2o5 = [sum(
    ciudad_materia_organica)/len(ciudad_materia_organica), sum(ciudad_p2o5)/len(ciudad_p2o5)]

# Séptimo, calcular los mínimos de las variables
# materia_organica y p2o5
min_materia_organica_p2o5 = [
    min(ciudad_materia_organica), min(ciudad_p2o5)]

# Octavo, calcular los máximos de las variables
# materia_organica y p2o5
max_materia_organica_p2o5 = [
    max(ciudad_materia_organica), max(ciudad_p2o5)]

# Noveno, realizar el conteo de cada una de las
# categorías
n_sumamente_apto = 0
n_moderadamente_apto = 0
n_marginalmente_apto = 0
n_no_apto = 0

for i in range(0, len(ciudad_aptitud), 1):
    # sumamente apto
    if ciudad_aptitud[i] == 'sumamente apto':
        n_sumamente_apto = n_sumamente_apto + 1

    # moderadamente apto
    elif ciudad_aptitud[i] == 'moderadamente apto':
        n_moderadamente_apto = n_moderadamente_apto + 1

    # marginalmente apto
    elif ciudad_aptitud[i] == 'marginalmente apto':
        n_marginalmente_apto = n_marginalmente_apto + 1

    # no apto
    # Esta parte se deja de esta forma por si existe
    # otra categoría extraña o errores en los nombres
    # de las categorías
    elif ciudad_aptitud[i] == 'no apto':
        n_no_apto = n_no_apto + 1

# Se construye el vector de categorias
# y se ordena en base a lo solicitado
conteo_categorias = [["sumamente apto", n_sumamente_apto],
                     ["moderadamente apto", n_moderadamente_apto],
                     ["marginalmente apto", n_marginalmente_apto],
                     ["no apto", n_no_apto]]
# En esta parte se utilizó lo señalado en
# https://stackoverflow.com/questions/27999249/how-to-sort-list-of-tuples-by-several-keys
conteo_categorias.sort(key=lambda par: [-par[1], par[0]])

# Décimo, se se realiza la impresión de los resultados
# en base al formato solicitado

# Promedios
for i in range(0, len(promedio_materia_organica_p2o5), 1):
    if i != len(promedio_materia_organica_p2o5) - 1:
        print(f"{promedio_materia_organica_p2o5[i]:.2f}", end=" ")
    else:
        print(f"{promedio_materia_organica_p2o5[i]:.2f}", end="\n")

# Mínimos
for i in range(0, len(min_materia_organica_p2o5), 1):
    if i != len(min_materia_organica_p2o5) - 1:
        print(f"{min_materia_organica_p2o5[i]}", end=" ")
    else:
        # En esta parte codegrade solicita el mínimo
        # de p205 sin decimales
        print(f"{min_materia_organica_p2o5[i]:.0f}", end="\n")

# Máximos
for i in range(0, len(max_materia_organica_p2o5), 1):
    if i != len(max_materia_organica_p2o5) - 1:
        # En esta parte codegrade solicita el máximo
        # de p205 sin decimales
        print(f"{max_materia_organica_p2o5[i]}", end=" ")
    else:
        print(f"{max_materia_organica_p2o5[i]:.0f}", end="\n")

# Conteo de categorías
for i in range(0, len(conteo_categorias), 1):
    print(f"{conteo_categorias[i][0]} {conteo_categorias[i][1]}")

# Undécimo, se cierra el archivo
archivo.close()
