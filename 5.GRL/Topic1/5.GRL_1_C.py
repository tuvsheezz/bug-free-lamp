from heapq import heappush, heappop


class Edge:
    def __init__(self, to, dist):
        self.to = to
        self.dist = dist


class Info:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist

    def __lt__(self, another):
        return self.dist < another.dist


class Node:
    def __init__(self):
        self.children = []


class Graph:
    def __init__(self, n, directed=False):
        self.V = n
        self.inf = float("inf")
        self.edges = list([Node() for _ in range(n)])
        self.is_directed = directed

    def add_edge(self, u, v, c):
        self.edges[u].children.append(Edge(v, c))
        if not self.is_directed:
            self.edges[v].children.append(Edge(u, c))

    # O(VVV)
    def warshall_floyd(self):
        dist = [[self.inf] * n for _ in range(n)]
        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    dist[i][j] = 0

        for i in range(n):
            for j in range(n):
                for edge in self.edges[i].children:
                    if j == edge.to:
                        dist[i][j] = edge.dist

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(len(dist)):
            if dist[i][i] < 0:
                return None

        return dist


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n, True)
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.add_edge(u, v, c)

    dist = g.warshall_floyd()
    if dist is None:
        print("NEGATIVE CYCLE")
        exit()

    for i in range(n):
        for j in range(n):
            if dist[i][j] == g.inf:
                dist[i][j] = "INF"
        print(*dist[i])
