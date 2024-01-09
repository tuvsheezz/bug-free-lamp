class Node:
    def __init__(self, id):
        self.id = id
        self.children = []


class Graph:
    def __init__(self, n, is_directed=False):
        self.vertices = n
        self.is_directed = is_directed
        self.edges = [Node(i) for i in range(n)]
        self.visited = [False for _ in range(n)]
        self.preorder = []
        self.inorder = []
        self.postorder = []

    def add_edge(self, u, v):
        self.edges[u].children.append(v)

        if not self.is_directed:
            self.edges[v].children.append(u)

    def dfs(self, root):
        self.preorder.append(root)
        self.visited[root] = True

        if self.edges[root].children[0] != -1:
            self.dfs(self.edges[root].children[0])

        self.inorder.append(root)

        if self.edges[root].children[1] != -1:
            self.dfs(self.edges[root].children[1])

        self.postorder.append(root)


if __name__ == "__main__":
    n = int(input())
    g = Graph(n, True)

    has_parent = [False for _ in range(n)]

    for _ in range(n):
        u, *v = map(int, input().split())
        for x in v:
            if x != -1:
                has_parent[x] = True
            g.add_edge(u, x)

    root = -1

    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    g.dfs(root)

    print("Preorder")
    print(" {}".format(" ".join(map(str, g.preorder))))
    print("Inorder")
    print(" {}".format(" ".join(map(str, g.inorder))))
    print("Postorder")
    print(" {}".format(" ".join(map(str, g.postorder))))
