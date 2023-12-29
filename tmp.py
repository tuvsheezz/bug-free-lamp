n, m = map(int, input().split())
a = [[] for _ in range(n)]

for _ in range(m):
    v = list(map(int, input().split()))
    if v[0] == 0:
        a[v[1]].append(v[2])
    elif v[0] == 1:
        print(" ".join(map(str, a[v[1]])))
    else:
        a[v[1]] = []
