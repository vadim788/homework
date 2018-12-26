def matri(rows):
    matri = []
    for i in range(0, rows):
        matri.append(list(map(int, input().rstrip().split())))
    return matri


def swap_columns(a, i, j):
    for z in range(0, len(a[0])):
        new = a[z][i - 1]
        a[z][i - 1] = a[z][j - 1]
        a[z][j - 1] = new
    return a


dimension = (input("Введіть кількість рядків та стовпчиків: ")).split(" ")
matri = matri(int(dimension[0]))
i = int(input("Введіть i: "))
j = int(input("Введіть j: "))
matri = swap_columns(matri, i, j)
for i in range(0, int(dimension[0])):
    print("".join(str(matri[i])))