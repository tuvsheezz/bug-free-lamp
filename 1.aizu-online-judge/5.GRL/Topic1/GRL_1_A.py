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

    def dijkstra(self, s):
        dist = list([self.inf] * self.V)
        prev = list([-1] * self.V)
        dist[s] = 0

        next_to_visit = []
        heappush(next_to_visit, Info(s, 0))

        while len(next_to_visit) > 0:
            current_node = heappop(next_to_visit)

            if dist[current_node.node] < current_node.dist:
                continue

            for edge in self.edges[current_node.node].children:
                if dist[edge.to] > dist[current_node.node] + edge.dist:
                    dist[edge.to] = dist[current_node.node] + edge.dist
                    prev[edge.to] = current_node.node
                    heappush(next_to_visit, Info(edge.to, dist[edge.to]))

        return dist, prev


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    g = Graph(n, True)
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.add_edge(u, v, c)

    dist, _ = g.dijkstra(s)
    for i in range(n):
        if dist[i] == g.inf:
            print("INF")
        else:
            print(dist[i])
