from collections import deque


class BinaryTreeNode:
    def __init__(self, id):
        self.id = id
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = "leaf"
        self.children = []


class BinaryTree:
    def __init__(self, n):
        self.vertices = n
        self.edges = [BinaryTreeNode(i) for i in range(n)]
        self.height = 0

    def add_edge(self, par, u, v):
        if not u == -1:
            self.edges[par].children.append(u)
            self.edges[par].children.append(v)
            self.edges[par].degree += 2
            self.edges[par].type = "internal node"
            self.edges[u].parent = par
            self.edges[v].parent = par
            self.edges[u].sibling = v
            self.edges[v].sibling = u

    def set_depth(self, root):
        queue = deque([root])

        self.edges[root].type = "root"

        while queue:
            current_node = queue.popleft()
            for x in self.edges[current_node].children:
                self.edges[x].depth = self.edges[current_node].depth + 1
                self.height = max(self.height, self.edges[x].depth)
                queue.append(x)

        for i in range(self.vertices):
            self.edges[i].height = self.height - self.edges[i].depth


if __name__ == "__main__":
    n = int(input())
    bt = BinaryTree(n)
    has_parent = [False for _ in range(n)]

    for _ in range(n):
        id, u, v = map(int, input().split())
        bt.add_edge(id, u, v)
        if not u == -1:
            has_parent[u] = True
        if not v == -1:
            has_parent[v] = True

    root = -1

    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    bt.set_depth(root)

    for i in range(n):
        li = [
            "node {}: parent = {}".format(i, bt.edges[i].parent),
            "sibling = {}".format(bt.edges[i].sibling),
            "degree = {}".format(bt.edges[i].degree),
            "depth = {}".format(bt.edges[i].depth),
            "height = {}".format(bt.edges[i].height),
            bt.edges[i].type,
        ]

        print(", ".join(li))
