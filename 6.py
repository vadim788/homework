a = input().split()
b = [[int(j) for j in input().split()] for i in range(int(a[0]))]
max_i = 0
max_j = 0
for i in range(int(a[0])):
    for j in range(int(a[1])):
        if b[i][j] > b[max_i][max_j]:
            max_i = i
            max_j = j
print(max_i, max_j)