from heapq import heappush, heappop


class Edge:
    def __init__(self, to, dist):
        self.to = to
        self.dist = dist


class Info:
    def __init__(self, node, dist, parent):
        self.node = node
        self.dist = dist
        self.parent = parent

    def __lt__(self, another):
        return self.dist < another.dist


class Node:
    def __init__(self, id):
        self.id = id
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

    def prim(self):
        par = list([-1] * self.V)
        visited = list([False] * self.V)
        min_weight = 0

        next_to_visit = []
        heappush(next_to_visit, Info(0, 0, -1))

        while len(next_to_visit) > 0:
            current_node = heappop(next_to_visit)

            if visited[current_node.node]:
                continue

            visited[current_node.node] = True
            par[current_node.node] = current_node.parent
            min_weight += current_node.dist

            for edge in self.edges[current_node.node].children:
                heappush(next_to_visit, Info(edge.to, edge.dist, current_node.node))

        return min_weight, par


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.add_edge(u, v, c)

    min_weight, _ = g.prim()

    print(min_weight)
