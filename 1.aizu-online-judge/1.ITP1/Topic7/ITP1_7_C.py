r, c = map(int, input().split())
sp = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    sp[i].append(sum(sp[i]))

sp.append([sum(sp[i][j] for i in range(r)) for j in range(c + 1)])

for i in range(r + 1):
    print(*sp[i])
