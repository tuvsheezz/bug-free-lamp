n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(m)]
c = [0 for _ in range(n)]

for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]
print(*c, sep='\n')
