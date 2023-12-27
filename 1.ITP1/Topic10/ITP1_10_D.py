def dist(p, X, Y):
    s = 0
    for x, y in zip(X, Y):
        s += abs(x - y) ** p
    return s ** (1 / p)


N = int(input())
(*X,) = map(int, input().split())
(*Y,) = map(int, input().split())
print(dist(1, X, Y))
print(dist(2, X, Y))
print(dist(3, X, Y))
print(max(abs(x - y) for x, y in zip(X, Y)))
