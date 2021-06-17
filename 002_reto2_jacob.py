n = float(input())

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
  while( i <= n):
    
    join_1 = float(input())
    join_2 = float(input())

    var_1 = join_1
    var_2 = join_2

    if ((var_1<3) or (var_2<46)):
      NA = NA+1
    elif ((3<=var_1<=4) or (46<=var_2<=57)):
      MA = MA+1
    elif ((4<var_1<=5) or (58<=var_2<=69)):
      MODA = MODA+1
    elif ((5<var_1) or (69<var_2)):
      SUMAp = SUMAp+1

    suma_1 = join_1 + suma_1
    suma_2 = join_2 + suma_2
    
    i =  i +1

  prom1 = suma_1/n
  prom2 = suma_2/n

  rouprom1 = round(prom1,2)
  rouprom2 = round(prom2,2)

  print(rouprom1)
  print(rouprom2)
  print("sumamente apto",SUMAp)
  print("moderadamente apto",MODA)
  print("marginalmente apto",MA)  
  print("no apto",NA)



