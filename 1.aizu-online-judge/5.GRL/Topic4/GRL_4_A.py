from collections import deque

inf = float("inf")


class Node:
    def __init__(self, id):
        self.id = id
        self.degree = 0
        self.children = []


class Graph:
    def __init__(self, n, is_directed=False):
        self.vertices = n
        self.is_directed = is_directed
        self.nodes = [Node(i) for i in range(n)]

    def add_edge(self, u, v):
        self.nodes[u].children.append(v)
        self.nodes[v].degree += 1

        if not self.is_directed:
            self.nodes[v].children.append(u)
            self.nodes[u].degree += 1

    # is_DAG?
    def bfs(self):
        queue = deque([])
        cnt = 0
        for node in self.nodes:
            if node.degree == 0:
                queue.append(node.id)

        while queue:
            current_node = queue.popleft()
            cnt += 1
            for x in self.nodes[current_node].children:
                self.nodes[x].degree -= 1
                if self.nodes[x].degree == 0:
                    queue.append(x)
        return cnt == self.vertices


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = Graph(n, True)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    if graph.bfs():
        print(0)
    else:
        print(1)
