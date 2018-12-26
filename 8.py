x = input().split()
n = int(x[0])
m = int(x[1])
a = [[[] for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2 == 0:
            a[i][j] = '.'
        else:
            a[i][j] = '*'
for row in a:
    print(' '.join(row))