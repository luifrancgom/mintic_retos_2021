# Librerias
import pandas as pd

# Primero, escoger una ciudad
# No se incluyen mensajes en los inputs
# ciudad = input()
ciudad = "Barranquilla"

# Segundo, importar el archivo, seleccionar las variables
# de interés y filtrar ciudad de interés
# Se utilizó la información señalada en
# https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html
datos_reto5 = (pd.read_csv('data.csv')
               # Seleccionar variables
               .loc[:, ['capital', 'materia_organica', 'p2o5', 'aptitud']]
               # Se requiere indicarle a pandas que nos referimos a la
               # variable ciudad con @
               .query('capital == @ciudad'))

# Tercero, calcular mínimos y maximos
# materia_organica y p2o5
# En esta parte se utilizó lo señalado en
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html
promedio_min_max = (datos_reto5
                    .agg({'materia_organica': ['mean', 'min', 'max'],
                          'p2o5': ['mean', 'min', 'max']}))

# cuarto, calcular conteo de categorías
# aptitud
conteo_aptitud = (datos_reto5
                  .loc[:, ['aptitud', 'capital']]
                  # Se utilizo lo señalado en
                  # https://www.statology.org/pandas-groupby-count/
                  .groupby(['aptitud'])
                  .size()
                  .reset_index(name='conteo')
                  # Se utilizo lo señalado en
                  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
                  .sort_values(by=["conteo", "aptitud"],
                               ascending=[False, True]))

# Quinto, se realiza la impresión de los resultados
# en base al formato solicitado

# Promedios, mínimos y máximos
for i in range(promedio_min_max.shape[0]):
    for j in range(promedio_min_max.shape[1]):
        if i == 0:
            if j == 0:
                print(f"{promedio_min_max.iloc[i][j]:.2f}", end=" ")
            if j == 1:
                print(f"{promedio_min_max.iloc[i][j]:.2f}", end="\n")
        if i in [1, 2]:
            if j == 0:
                print(f"{promedio_min_max.iloc[i][j]}", end=" ")
            if j == 1:
                # Esto se requiere por que codegrade no acepta
                # datos tipo float sino solo enteros
                print(f"{promedio_min_max.iloc[i][j]:.0f}", end="\n")

# Conteo de categorías
for i in range(conteo_aptitud.shape[0]):
    for j in range(conteo_aptitud.shape[1]):
        if j == 0:
            print(f"{conteo_aptitud.iloc[i][j]}", end=" ")
        if j == 1:
            print(f"{conteo_aptitud.iloc[i][j]}", end="\n")
