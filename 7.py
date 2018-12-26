n = int(input())
a = [['.' for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i == n-j-1 or i == (n-1)/2 or j == (n-1)/2:
            a[i][j] = '*'
for row in a:
    print(' '.join([str(elem) for elem in row]))