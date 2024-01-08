class UnionFind:
    def __init__(self, n):
        self.parent = list([-1 for _ in range(n)])
        self.size = list([1 for _ in range(n)])
        self.count = n
        self.size_max = 1

    def root(self, x):
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        if self.size[x] == self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        self.size_max = max(self.size_max, self.size[x])
        self.count -= 1

    def count_of_group(self):
        return self.count

    def get_union_size(self, x):
        return self.size[self.root(x)]


class Kruskal:
    def __init__(self, n):
        self.n = n
        self.edges = list([])
        self.uf = UnionFind(n)

    def add_edge(self, u, v, cost):
        self.edges.append((cost, u, v))

    def build(self):
        total_cost = 0
        self.edges = sorted(self.edges)
        for cost, u, v in self.edges:
            if not self.uf.same(u, v):
                self.uf.unite(u, v)
                total_cost += cost
        return total_cost


if __name__ == "__main__":
    n = int(input())

    kruskal = Kruskal(n)

    print(kruskal.build())
