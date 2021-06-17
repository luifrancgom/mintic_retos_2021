m = float(input())
p = float(input())

if (m<3 or p <46):
    print("No apto")
elif (3<=m<=4 or 46<=p<=57):
    print("Marginalmente apto")
elif (4<m<=5 or 57<p<=69):
    print("Moderadamente apto")
elif (5<m or 69<p):
    print("Sumamente apto")

