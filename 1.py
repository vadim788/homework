def matri(rows):
    matri = []
    for i in range(0,rows):
        matri.append(list(map(int, input().rstrip().split())))
    return matri
dimension = (input("Введіть кількість рядків та стовпчиків: ")).split(" ")
matri = matri(int(dimension[0]))
mx = max(map(max, matri))
for i, e in enumerate(matri):
    try:
        j = e.index(mx)
        break
    except ValueError:
        pass
print(i,j)