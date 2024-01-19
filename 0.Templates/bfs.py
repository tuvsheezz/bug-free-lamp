from collections import deque

inf = float("inf")


class Node:
    def __init__(self, id: int):
        self.id: int = id
        self.children: list[int] = []


class Graph:
    def __init__(self, n: int, is_directed: bool = False):
        self.vertices: int = n
        self.is_directed: bool = is_directed
        self.edges: list[Node] = [Node(i) for i in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.edges[u].children.append(v)

        if not self.is_directed:
            self.edges[v].children.append(u)

    def bfs(self, root: int) -> list[int]:
        visited: list[bool] = [False for _ in range(self.vertices)]
        dist: list[int] = [int(inf) for _ in range(self.vertices)]

        dist[root] = 0
        queue = deque([root])

        while queue:
            current_node = queue.popleft()
            visited[current_node] = True
            for x in self.edges[current_node].children:
                if not visited[x]:
                    dist[x] = min(dist[x], dist[current_node] + 1)
                    queue.append(x)
        return dist


if __name__ == "__main__":
    n = int(input())
    graph = Graph(n, True)

    for _ in range(n):
        u, k, *v = map(int, input().split())
        for x in v:
            graph.add_edge(u - 1, x - 1)

    dist = graph.bfs(0)

    for i in range(n):
        print(i + 1, -1 if dist[i] == inf else dist[i])
