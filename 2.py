n = int(input("Введіть n: "))
matri = []
for i in range(0,n):
    matri.append(["."]*n)
a = n//2
matri[a]=["*"]*n
for i in range(0,n):
    matri[i][a]="*"
    matri[i][i]="*"
    matri[i][n-i-1]="*"
for i in range(0,n):
    print(" ".join(matri[i]))