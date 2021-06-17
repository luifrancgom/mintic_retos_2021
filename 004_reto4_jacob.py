n = 1
total_NA = 0
total_MARG = 0
total_MOD = 0
total_SA = 0

new_mo = 0
matriz_mo = []

new_po2 = 0
matriz_po2 = []

catmas = []
catmen = []

mo = 0

zonas = int(input())
dias = 7
for i in range(zonas):
    matriz_mo.append([])
    matrix_mo = str(input()).split(" ")
    
    for j in range(dias):
        new_mo = float(matrix_mo[j])
        
        matriz_mo[i].append(new_mo)
for i in range(zonas):
    matriz_po2.append([])
    matrix_po2 = str(input()).split(" ")
    
    for j in range(dias):
        new_po2 = float(matrix_po2[j])
        
        matriz_po2[i].append(new_po2)

for i in range(zonas):
    mo1 = matriz_mo[i]
    po21 = matriz_po2[i]
    for i in range(dias):
        mo = mo1[i]
        po2 = po21[i]
      
        if ((mo < 3) or (po2 < 46)):
            total_NA = total_NA + 1
        elif ((3 <= mo <=4) or (46 <= po2 <= 57)):
            total_MARG = total_MARG +1
        elif ((4 < mo<=5) or (57 < po2 <= 69)):
            total_MOD = total_MOD +1
        elif ((5 < mo) or (69 < po2)):
            total_SA = total_SA +1
               
print(total_NA,total_MARG,total_MOD,total_SA)

for i in range(zonas):
    mo1 = matriz_mo[i]
    po21 = matriz_po2[i]
    total_NA = 0
    total_MARG = 0
    total_MOD = 0
    total_SA = 0
    for i in range(dias):
       
        mo = mo1[i]
        po2 = po21[i]
        if ((mo < 3) or (po2 < 46)):
            total_NA = total_NA + 1
        elif ((3 <= mo <= 4) or (46 <= po2 <= 57)):
            total_MARG = total_MARG +1
        elif ((4 < mo<=5) or (57 < po2 <= 69)):
            total_MOD = total_MOD +1
        elif ((5 < mo) or (69 < po2)):
            total_SA = total_SA +1

    if (total_SA>=total_MOD and total_SA>=total_MARG and total_SA>=total_NA):
        catmas.append("sumamente apto")
    elif (total_MOD>=total_SA and total_MOD>=total_MARG and total_MOD>=total_NA):
        catmas.append("moderadamente apto")
    elif (total_MARG>=total_SA and total_MARG>=total_MOD and total_MARG>=total_NA):       
        catmas.append("marginalmente apto")
    elif (total_NA>=total_SA and total_NA>=total_MOD and total_NA>=total_MARG):        
        catmas.append("no apto")
    if total_NA ==0:
        total_NA = 100000000
    if total_MARG ==0:
        total_MARG = 10000000
    if total_MOD ==0:
        total_MOD = 10000000
    if total_SA ==0:
        total_SA = 10000000
    if (total_SA<=total_MOD and total_SA<=total_MARG and total_SA<=total_NA):
        catmen.append("sumamente apto")
    elif(total_MOD<=total_SA and total_MOD<=total_MARG and total_MOD<=total_NA ):
        catmen.append("moderadamente apto")
    elif(total_MARG<=total_SA and total_MARG<=total_MOD and total_MARG<=total_NA ):       
        catmen.append("marginalmente apto")
    elif (total_NA<=total_SA and total_NA<=total_MOD and total_NA<=total_MARG ):        
        catmen.append("no apto")

c="" 
for x in range(len(catmas)) :
  c = c+"".join(catmas[x])
  if x<zonas-1:
      c = c+"," 

print(c) 

men="" 
for x in range(len(catmen)) :
  men = men+"".join(catmen[x])
  if x<zonas-1:
      men = men+"," 

print(men) 



# 3
# 5.62 2.33 1.97 4.78 4.21 1.64 4.26
# 2.09 7.12 7.13 3.62 1.87 4.11 2.14
# 5.09 3.19 5.17 4.5 4.99 3.21 5.24
# 63 58 42 64 46 45 62
# 72 42 53 77 77 43 56
# 59 56 58 67 48 79 49