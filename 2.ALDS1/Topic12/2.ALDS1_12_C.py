from heapq import heappush, heappop


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
        self.edges[u].children.append((v, c))
        if not self.is_directed:
            self.edges[v].children.append((u, c))

    def dijkstra(self, s):
        dist = list([self.inf] * self.V)
        prev = list([-1] * self.V)
        dist[s] = 0

        next_to_visit = []
        heappush(next_to_visit, (0, s))

        while len(next_to_visit) > 0:
            current_node = heappop(next_to_visit)
            v = current_node[1]

            if dist[v] < current_node[0]:
                continue

            for edge in self.edges[v].children:
                if dist[edge[0]] > dist[v] + edge[1]:
                    dist[edge[0]] = dist[v] + edge[1]
                    prev[edge[0]] = v
                    heappush(next_to_visit, (dist[edge[0]], edge[0]))

        return dist, prev


if __name__ == "__main__":
    n = int(input())
    g = Graph(n, True)
    for i in range(n):
        u, k, *v_c = map(int, input().split())
        for j in range(k):
            g.add_edge(u, v_c[2 * j], v_c[2 * j + 1])

    dist, _ = g.dijkstra(0)
    for i in range(n):
        print(i, dist[i])
