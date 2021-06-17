#Como se sabe la cantidad de datos a ingresar por lista si no hay variable de ingreso
# como hacer que un print de un round con dos
# decimales imprima un cero como segundo
# decimal ej 1,2 ------ 1,20 
# VERIFICAR RANGOS DE ELEMENTOS


n = int(input())

ar_mo = []
ar_po2 = []

total_mo = []
total_po2 = []

total_mo_a = []
total_po2_a = []

mo_ha = []
po2_ha = []
i=1

NA = 0
MA =0
MODA= 0
SUMAp= 0

suma_1 = 0
suma_2 = 0

if n == 0:
  print("0")
  print("0")
  print("sumamente apto",SUMAp)
  print("moderadamente apto",MODA)
  print("marginalmente apto",MA)  
  print("no apto",NA)
  
elif n != 0:
    for k in range(n):

        j = input().split(" ")
        suma = 0
        
        for i in range(len(j)):
            floats = float(j[i])
            suma = floats + suma
        tot = float(len(j))

        prom_mo_sin = (suma/tot)

        prom_mo =  "{0:.2f}".format(prom_mo_sin)

        total_mo_a.append(prom_mo)
        
       

      # po2
        
        po2_ini = input().split(" ")
        suma_po2 = 0
        for i in range(len(po2_ini)):
            floats_po2 = float(po2_ini[i])
            suma_po2 = suma_po2+ floats_po2 
        tot_po2 = float(len(po2_ini))



        prom_po2_sin = ((suma_po2/tot_po2))

        prom_po2 =  "{0:.2f}".format(prom_po2_sin)

        total_po2.append(prom_po2)
    
  
    for i in range(len(total_po2_a)):
        po2_a = float(total_po2_a[i])
        po2_a =  "{0:.2f}".format(po2_a)
        total_po2.append(po2_a)

    for i in range(len(total_mo_a)):
        mo_a = float(total_mo_a[i])
        mo_a =  "{0:.2f}".format(mo_a)        
        total_mo.append(mo_a)


    

   

    x = ""

    for i in range(len(total_mo)):
        x = x + str(total_mo[i])+ " "
        
    print(x)
    y = ""
    for i in range(len(total_po2)):
        y = y + str(total_po2[i])+ " "
        
    print(y)

    for i in range(len(total_po2)):
        po2_a_s = float(total_po2[i])
        po2_ha.append(po2_a_s)

    for i in range(len(total_mo)):
        mo_a = float(total_mo[i])
        mo_ha.append(mo_a)




    for i in range(len(total_mo)):
        
        join_1 = mo_ha[i]
        join_2 = po2_ha[i]

        var_1 = join_1
        var_2 = join_2
        
        if ((var_1 < 3) or (var_2 < 46)):
          NA = NA+1
        elif ((3<=var_1<4) or (46<=var_2<=57)):
            MA = MA+1
        elif ((4<=var_1<=5) or (57<var_2<=69)):
            MODA = MODA+1
        else:
            SUMAp = SUMAp+1
    
    print("sumamente apto",SUMAp)
    print("moderadamente apto",MODA)
    print("marginalmente apto",MA)  
    print("no apto",NA)
