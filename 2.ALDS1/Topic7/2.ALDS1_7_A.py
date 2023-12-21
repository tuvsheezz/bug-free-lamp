from collections import deque


class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = []


class Graph:
    def __init__(self, n, is_directed=False):
        self.vertices = n
        self.is_directed = is_directed
        self.edges = [Node(-1) for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].children.append(v)

        if not self.is_directed:
            self.edges[v].children.append(u)

    def bfs(self, root):
        queue = deque([root])
        self.edges[root].parent = -1
        visited = [False for _ in range(self.vertices)]
        dist = [0 for _ in range(self.vertices)]

        while queue:
            current_node = queue.popleft()
            visited[current_node] = True
            for x in self.edges[current_node].children:
                if not visited[x]:
                    self.edges[x].parent = current_node
                    dist[x] = dist[current_node] + 1
                    queue.append(x)
        return dist


if __name__ == "__main__":
    n = int(input())
    g = Graph(n, True)
    has_parent = [False for _ in range(n)]

    for _ in range(n):
        u, k, *v = map(int, input().split())
        for x in v:
            has_parent[x] = True
            g.add_edge(u, x)

    root = -1

    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    dist = g.bfs(root)

    for i in range(n):
        li = [
            "node {}: parent = {}".format(i, g.edges[i].parent),
            "depth = {}".format(dist[i]),
            "root"
            if g.edges[i].parent == -1
            else "internal node"
            if g.edges[i].children
            else "leaf",
            "[{}]".format(", ".join(map(str, g.edges[i].children))),
        ]

        print(", ".join(li))
