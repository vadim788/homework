dimension = (input("Введіть кількість рядків та стовпчиків: ")).split(" ")
matri = []
for i in range(0,int(dimension[0])):
    matri.append(["."]*(int(dimension[1])))
for i in range(0,int(dimension[0])):
    for j in range(0,int(dimension[1])):
        if (i+j)%2==1:
            matri[i][j]="*"
for i in range(0,int(dimension[0])):
    print(" ".join(matri[i]))