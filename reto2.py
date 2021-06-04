# no incluir mensajes en los inputs
# tambien se incluye int dado que las muestras deben
# ser números enteros
muestras = int(input())

# indicadores de la variable de conteo
# muestras
i = 0
# categorias
n_sumamente_apto = 0
n_moderadamente_apto = 0
n_marginalmente_apto = 0
n_no_apto = 0
# suma variables
suma_materia_organica = 0
suma_oxido_fosforo = 0

while (i < muestras):
    # no incluir mensajes en los inputs
    materia_organica = float(input())
    oxido_fosforo = float(input())

    # conteo de muestras
    i = i + 1

    # acumulacion suma de variables
    suma_materia_organica = suma_materia_organica + materia_organica
    suma_oxido_fosforo = suma_oxido_fosforo + oxido_fosforo

    # En esta parte utilice el código de Kariett Justine Pinto Pinto,
    # estudiante del curso, para mejorar esta sección relacionada con
    # el reto 1 para que fuera más compacta y corta la ejecución

    # sumamente apto
    if (materia_organica > 5 and oxido_fosforo > 69):
        n_sumamente_apto = n_sumamente_apto + 1

    # moderadamente apto
    elif (materia_organica > 4 and oxido_fosforo >= 58):
        n_moderadamente_apto = n_moderadamente_apto + 1

    # marginalmente apto
    elif (materia_organica >= 3 and oxido_fosforo >= 46):
        n_marginalmente_apto = n_marginalmente_apto + 1

    # no apto
    else:
        n_no_apto = n_no_apto + 1

# Esta parte la realice de esta forma para obtener exactamente
# las salidas esperadas donde seguí las indicaciones de
# Sebastian Joao Racedo Valbuena respecto a lo señalado en
# https://www.w3schools.com/python/ref_string_format.asp
# De esa manera por ejemplo obtengo 55.00 y no 55 si lo hiciera con
# round(x,2)
# promedio de la materia organica a 2 decimales
print(f"{suma_materia_organica/muestras:.2f}")
# promedio del oxido de fosforo a 2 decimales
print(f"{suma_oxido_fosforo/muestras:.2f}")
# conteo de categorias resultantes
print(f"sumamente apto {n_sumamente_apto}")
print(f"moderadamente apto {n_moderadamente_apto}")
print(f"marginalmente apto {n_marginalmente_apto}")
print(f"no apto {n_no_apto}")
