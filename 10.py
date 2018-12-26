n = int(input())
a = [0] * n
for i in range(n):
    a[i] = [0] * n
for i in range(n):
    for j in range(n):
        a[i][j] = abs(i - j)
for row in a:
    print(' '.join([str(elem) for elem in row]))