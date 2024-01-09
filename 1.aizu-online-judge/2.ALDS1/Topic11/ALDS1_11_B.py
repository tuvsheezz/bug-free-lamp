class Node:
    def __init__(self, id):
        self.id = id
        self.children = []


class Graph:
    def __init__(self, n, is_directed=False):
        self.vertices = n
        self.is_directed = is_directed
        self.edges = [Node(i) for i in range(n)]
        self.visited = [False for _ in range(n)]
        self.fi = [100000 for _ in range(n)]
        self.la = [0 for _ in range(n)]
        self.step = 1

    def add_edge(self, u, v):
        self.edges[u].children.append(v)

        if not self.is_directed:
            self.edges[v].children.append(u)

    def dfs(self, root):
        self.fi[root] = min(self.step, self.fi[root])
        self.step += 1

        self.visited[root] = True

        for child in self.edges[root].children:
            if not self.visited[child]:
                self.dfs(child)

        self.la[root] = max(self.step, self.la[root])
        self.step += 1


if __name__ == "__main__":
    n = int(input())
    g = Graph(n, True)

    for _ in range(n):
        u, k, *v = map(int, input().split())
        for x in v:
            g.add_edge(u - 1, x - 1)

    for i in range(n):
        if not g.visited[i]:
            g.dfs(i)

    for i in range(n):
        print(i + 1, g.fi[i], g.la[i])
