n = int(input("Введіть n: "))
matri = []
for i in range(0,n):
    matri.append([" "]*n)
for i in range(0,n):
    for j in range(0,n-i):
        matri[i][j]="0"
for i in range(1,n):
    for j in range(n-i,n):
        matri[i][j]="2"
for i in range(0,n):
    matri[i][n-i-1]="1"
for i in range(0,n):
    print(" ".join(matri[i]))