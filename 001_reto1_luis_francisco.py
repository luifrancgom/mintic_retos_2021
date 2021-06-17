# Definición de entradas por parte del usuario
materia_organica = float(input("Materia orgánica (% total): "))
oxido_de_fosforo = float(input("Óxido de fosforo (Kg/Ha): "))

# Definir el algoritmo
# Si ambas variables se encuentran dentro de la misma categoría
# se escogerá la categoría
# Si están en categorías diferentes se escogerá la peor de ellas.

# Definición de categorías caso porcentaje de materia orgánica
# En esta parte se acoto el valor hasta el 100% para evitar
# valores no válidos que puedan ser introducidos por el usuario
# final
if materia_organica > 5 and materia_organica <= 100:
    cat_srt_materia_organica = "Sumamente apto"
    cat_float_materia_organica = 4
elif materia_organica >= 4.1 and materia_organica <= 5:
    cat_srt_materia_organica = "Moderadamente apto"
    cat_float_materia_organica = 3
elif materia_organica >= 3 and materia_organica <= 4:
    cat_srt_materia_organica = "Marginalmente apto"
    cat_float_materia_organica = 2
# En esta parte se acoto el valor como mpinimo al 0% para evitar
# valores no válidos que puedan ser introducidos por el usuario
# final
elif materia_organica >= 0 and materia_organica < 3:
    # No apto
    cat_srt_materia_organica = "No apto"
    cat_float_materia_organica = 1
else:
    # Valor no valido
    # Esta parte no esta incluida pero es mejor
    # señalarle un error al usuario
    cat_srt_materia_organica = "Valor no válido"
    cat_float_materia_organica = 0

# Definición de categorías caso óxido de fosforo
# kilogramo por hectarea
if oxido_de_fosforo > 69:
    cat_srt_oxido_de_fosforo = "Sumamente apto"
    cat_float_oxido_de_fosforo = 4
elif oxido_de_fosforo >= 58 and oxido_de_fosforo <= 69:
    cat_srt_oxido_de_fosforo = "Moderadamente apto"
    cat_float_oxido_de_fosforo = 3
elif oxido_de_fosforo >= 46 and oxido_de_fosforo <= 57:
    cat_srt_oxido_de_fosforo = "Marginalmente apto"
    cat_float_oxido_de_fosforo = 2
# En esta parte se acoto el valor como mínimo al 0 para evitar
# valores no válidos que puedan ser introducidos por el usuario
# final
elif oxido_de_fosforo >= 0 and oxido_de_fosforo < 46:
    cat_srt_oxido_de_fosforo = "No apto"
    cat_float_oxido_de_fosforo = 1
else:
    # Valor no valido
    # Esta parte no esta incluida pero es mejor
    # señalarle un error al usuario
    cat_srt_oxido_de_fosforo = "Valor no válido"
    cat_float_oxido_de_fosforo = 0

# Definición de la categoría final
if cat_float_materia_organica == cat_float_oxido_de_fosforo:
    categoria = cat_srt_materia_organica
    print(categoria)
elif cat_float_materia_organica > cat_float_oxido_de_fosforo:
    categoria = cat_srt_oxido_de_fosforo
    print(categoria)
else:
    categoria = cat_srt_materia_organica
    print(categoria)


# Preguntas
# ¿Qué pasa con el total del porcentaje de la materia orgánica
# cuando esta en el intervalo abierto (4, 4.1)?
# Por ejemplo un valor de 4.05
# ¿Qué pasa cuando el óxido de fósforo medido en kilogramos por
# hectarea esta en el intervalo abierto (57, 58)?
# Por ejemplo un valor de 57.5
