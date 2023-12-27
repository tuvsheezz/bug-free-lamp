n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
c = [[0 for _ in range(l)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(l):
            c[i][k] += a[i][j] * b[j][k]

for i in range(n):
    print(*c[i])
