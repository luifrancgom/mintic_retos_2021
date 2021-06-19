import _csv, operator

#llamada de la .CSV y guardada en una matriz llamada CACAO
with open(r'data.csv',encoding='utf-8') as f:
    r = _csv.reader(f,delimiter=',')
    cacao = list(r)

#datos de entrada y varibales acumuladores de los resultados de los procesos
ciudad = str.title(input())
matma = []
matp2 = []
aptitud = {"no apto":0,"marginalmente apto":0,"moderadamente apto":0,"sumamente apto":0}

# proceso loop para llendo de acumuladores
for i in cacao:
    if str.title(i[0]) == ciudad:

        # acumulado de listas para valores referentes al dato de entrada
        matma.append(float(i[3]))
        matp2.append(float(i[4]))

        #acumuladores del diccionario de Aptitudes
        if (float(i[3]) < 3) or (float(i[4]) < 46):
            aptitud["no apto"] = aptitud["no apto"] + 1
        elif (float(i[3]) >= 3 and float(i[3]) <= 4) or (float(i[4]) >= 46 and float(i[4]) <= 57):
            aptitud["marginalmente apto"] = aptitud["marginalmente apto"] + 1
        elif (float(i[3]) > 4 and float(i[3]) <= 5) or (float(i[4]) > 57 and float(i[4]) <= 69):
            aptitud["moderadamente apto"] = aptitud["moderadamente apto"] + 1
        elif (float(i[3]) > 5) or (float(i[4]) > 69):
            aptitud["sumamente apto"] = aptitud["sumamente apto"] + 1

#procesos de promediar e imprimir los valores de Materia organica y P2O5
print("{:.2f}".format(sum(matma)/len(matma)), "{:.2f}".format(sum(matp2)/len(matp2)))

#procesos de minimos y maximos e imprimir los valores de Materia organica y P2O5
print(round(min(matma),2), "{:.0f}".format(min(matp2)))
print(round(max(matma),2), "{:.0f}".format(max(matp2)))

#proceso de determinar la aptitud en orden decendente e imprimirlo
aptitudhot = sorted(aptitud.items(), key=operator.itemgetter(1), reverse=True)
for llave in enumerate(aptitudhot):
    print(llave[1][0], aptitud[llave[1][0]])