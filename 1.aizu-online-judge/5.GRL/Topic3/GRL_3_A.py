"""
橋や関節点などを効率的に求める際に有効なアルゴリズム。
グラフをDFSして, ord[idx] := DFS で頂点に訪れた順番,
low[idx] := 頂点 idx からDFS木の葉方向の辺を 0 回以上,
後退辺を 1 回以下通って到達可能な頂点の ord の最小値 を各頂点について求める。
ある頂点 u が関節点であるとき,DFS木の根については子が 2つ以上,
それ以外の頂点については 頂点 u のある子 v について ord[u] ≤ low[v] を満たす。
ある辺(u, v) が橋であるとき, ord[u] < low[v] を満たす。
"""
import sys

sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, id):
        self.id = id
        self.children = []


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:
    def __init__(self, n, is_directed=False):
        self.vertices = n
        self.is_directed = is_directed
        self.edges = [Node(i) for i in range(n)]
        self.ans = 0
        self.ord = [0] * n
        self.low = [0] * n
        self.articulations = []  # 関節点
        self.bridges = []  # 橋
        self.visited = [False] * n

    def add_edge(self, u, v):
        self.edges[u].children.append(v)

        if not self.is_directed:
            self.edges[v].children.append(u)

    def low_link(self):
        k = 0
        for i in range(self.vertices):
            if not self.visited[i]:
                k = self.dfs(i, k, -1)

    def dfs(self, idx, k, par):
        self.visited[idx] = True
        self.ord[idx] = k
        self.low[idx] = self.ord[idx]
        k += 1
        is_articulation = False
        cnt = 0

        for to in self.edges[idx].children:
            if not self.visited[to]:
                cnt += 1
                k = self.dfs(to, k, idx)
                self.low[idx] = min(self.low[idx], self.low[to])
                is_articulation |= ~par and self.low[to] >= self.ord[idx]
                if self.ord[idx] < self.low[to]:
                    self.bridges.append(Edge(idx, to))
            elif to != par:
                self.low[idx] = min(self.low[idx], self.ord[to])

            is_articulation |= par == -1 and cnt > 1
            if is_articulation:
                self.articulations.append(idx)

        return k


if __name__ == "__main__":
    n, m = map(int, input().split())
    G = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        G.add_edge(u, v)

    G.low_link()

    for x in sorted(set(G.articulations)):
        print(x)

    # for edge in G.bridges:
    #     print(edge.u, edge.v)

# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
# G.articulations

# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_B
# G.bridges
