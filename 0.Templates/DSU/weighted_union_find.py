class WeightedUnionFind:
    def __init__(self, n):
        self.parent = list([-1 for _ in range(n)])
        self.size = list([1 for _ in range(n)])
        self.rank = list([0 for _ in range(n)])
        self.weights = list([0 for _ in range(n)])
        self.count = n
        self.size_max = 1

    def root(self, x):
        if self.parent[x] == -1:
            return x
        else:
            r = self.root(self.parent[x])
            self.weights[x] += self.weights[self.parent[x]]
            self.parent[x] = r
            return r

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y, weight=0):
        rx, ry = self.root(x), self.root(y)
        if rx == ry:
            return

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.weights[rx] = weight - self.weights[x] + self.weights[y]
        else:
            self.parent[ry] = rx
            self.weights[ry] = -weight - self.weights[y] + self.weights[x]

            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def diff(self, x, y):
        return self.weights[x] - self.weights[y]


if __name__ == "__main__":
    n, q = map(int, input().split())
    uft = WeightedUnionFind(n)
    for _ in range(q):
        type_, u, v, *weight = map(int, input().split())
        if type_ == 0:
            uft.unite(u, v, weight[0])
        else:
            print(uft.diff(u, v) if uft.same(u, v) else "?")
