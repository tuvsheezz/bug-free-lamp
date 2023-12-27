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

    # ベルマン・フォード法
    # 辺の重みに負数が存在する場合の
    # 単一始点最短経路探索
    def bellman_ford(self, r):
        dist = [self.inf] * self.V
        dist[r] = 0

        # 辺の最短距離を求める処理（緩和）
        # (辺の数 - 1)回繰り返す
        for _ in range(self.V - 1):
            for current_node in range(self.V):
                for edge in self.edges[current_node].children:
                    if (
                        dist[current_node] != self.inf
                        and dist[edge.to] > dist[current_node] + edge.dist
                    ):
                        dist[edge.to] = dist[current_node] + edge.dist

        # 負の重みの閉路（経路上の辺の重みの和が負になるような閉路）を探索
        # 辺の重みの緩和の余地が1回でもあるなら、負の閉路がある
        for current_node in range(n):
            for edge in self.edges[current_node].children:
                if (
                    dist[current_node] != self.inf
                    and dist[edge.to] > dist[current_node] + edge.dist
                ):
                    return None
        return dist


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    g = Graph(n, True)
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.add_edge(u, v, c)

    dist = g.bellman_ford(s)
    if dist is None:
        print("NEGATIVE CYCLE")
        exit()

    for i in range(n):
        if dist[i] == g.inf:
            print("INF")
        else:
            print(dist[i])
