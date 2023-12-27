import sys


class Node:
    def __init__(self):
        self.children = []


class Graph:
    def __init__(self, n, is_directed=False):
        self.vertices = n
        self.is_directed = is_directed
        self.edges = [Node() for _ in range(n)]
        self.visited = [False for _ in range(n)]
        self.group = [-1 for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].children.append(v)

        if not self.is_directed:
            self.edges[v].children.append(u)

    def dfs(self, root, group_id):
        self.visited[root] = True
        self.group[root] = group_id

        for child in self.edges[root].children:
            if not self.visited[child]:
                self.dfs(child, group_id)


if __name__ == "__main__":
    sys.setrecursionlimit(200100)
    n, m = map(int, input().split())
    g = Graph(n, False)

    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    for i in range(n):
        if not g.visited[i]:
            g.dfs(i, i)

    q = int(input())
    for i in range(q):
        u, v = map(int, input().split())
        if g.group[u] == g.group[v]:
            print("yes")
        else:
            print("no")
