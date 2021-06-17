#import pandas as pd
#import numpy as np
import csv

#Definición de variables y matrices a utilizar
MatrizData = []
MatrizCiudad = []
PromedioMO=[]
Resultados=[]
PromMO=0
PromP2O5=0
Sumamente=0
Moderadamente=0
Marginalmente=0
NoApto=0

#Lectura del archivo; utilizar 'r' para indicar que sólamente se leerá el archivo
Archivo = csv.reader(open('data.csv','r'))

#Escrbir todo el csv en una matriz dentro de Python (no es lo mejor)
for Columna in Archivo:
    MatrizData.append(Columna)

#Indicar el nombre de la ciudad a consultar
Ciudad=input()

#Se recorrerá toda la MatrizData (aquella que contiene toda la data del CSV) y se comparará la columna 0 (donde están registradas las ciudades)
#con la entrada recibida en la variable Ciudad. Si X registro coincide, entonces, tal registro se inscribirá en la MatrizCiudad
for i in range(1,len(MatrizData)):
    if MatrizData[i][0]==Ciudad:
        MatrizCiudad.append(MatrizData[i])

#DEFINICIÓN DE MÍNIMOS Y MÁXIMOS DE MO Y P2O5
#Las siguientes variables tomarán los primeros valores registrados de MO y P2O5 correspondientes a la MatrizCiudad
MinMO=float(MatrizCiudad[0][3])
MinP2O5=int(MatrizCiudad[0][4])
MaxMO=float(MatrizCiudad[0][3])
MaxP2O5=int(MatrizCiudad[0][4])

#Recorremos los registros de la MatrizCiudad
for i in range(0,len(MatrizCiudad)):

    #Sumamos los valores de MO y P2O5 con base en la info de las columnas 3 y 4 para, al final, hallar el promedio (Ver línea XX)
    PromMO=PromMO + float(MatrizCiudad[i][3])
    PromP2O5=PromP2O5 + int(MatrizCiudad[i][4])

    #DEFINICIÓN DE MÍNIMOS
    #Lo que haremos será comparar si el valor del i registro para MO y P2O5 es MENOR al valor que ya hemos definido para las variables
    #"Min" de cada elemento. Si lo es, entonces dicho valor se reescribirá en la variable en cuestión
    if float(MatrizCiudad[i][3]) < MinMO:
        MinMO=float(MatrizCiudad[i][3])
    if int(MatrizCiudad[i][4]) < MinP2O5:
        MinP2O5=int(MatrizCiudad[i][4])

    #DEFINICIÓN DE MÁXIMOS
    #Lo que haremos será comparar si el valor del i registro para MO y P2O5 es MAYOR o IGUAL al valor que ya hemos definido para las variables
    #"Max" de MO y P2O5. Si lo es, entonces dicho valor se reescribirá en la variable en cuestión
    if float(MatrizCiudad[i][3]) >= MaxMO:
        MaxMO=float(MatrizCiudad[i][3])
    if int(MatrizCiudad[i][4]) >= MaxP2O5:
        MaxP2O5=int(MatrizCiudad[i][4])

    #CONTADOR DE CATEGORIAS
    #De acuerdo a la info de la columna 6 de nuestra matriz/CSV ("Aptitud" en CSV), se cuentan las categorías mediante condicional IF
    if MatrizCiudad[i][6]=="sumamente apto":
        Sumamente=Sumamente+1
    if MatrizCiudad[i][6]=="moderadamente apto":
        Moderadamente=Moderadamente+1
    if MatrizCiudad[i][6]=="marginalmente apto":
        Marginalmente=Marginalmente+1
    if MatrizCiudad[i][6]=="no apto":
        NoApto=NoApto+1

#Se cierra el recorrido

#Creamos una pequeña matríz tupla donde almacenamos los valores de las categorías...
Resultados = [('sumamente apto',Sumamente),('moderadamente apto',Moderadamente),("marginalmente apto",Marginalmente),("no apto",NoApto)]
#Luego, la ordenamos de mayor a menor considerando las cantidades de cada categoría (recordar que sorted ordena de menor a mayor)
Resultados = sorted(Resultados, key=lambda x: x[1], reverse=True)

#Terminamos de ajustar el promedio de MO y P2O5, dividiendo sobre la cantidad de registros existentes en la MatrizCiudad
PromMO=PromMO/len(MatrizCiudad)
PromP2O5=PromP2O5/len(MatrizCiudad)

#Imprimimos los resultados
print(format((PromMO),'.2f'),format((PromP2O5),'.2f'))
print(MinMO,MinP2O5)
print(MaxMO,MaxP2O5)

#Imprimmos la matriz donde almacenamos la categoría y sus cantidades
for i in range(len(Resultados)):
    print(*Resultados[i], sep=" ")