class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.ino = None
        self.preo = None

    def insert(self, z):
        x = self.root
        y = None
        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
            z.parent = y

        z.parent = y

        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        self.ino.append(root.data)
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return

        self.preo.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def print(self):
        self.ino = list()
        self.preo = list()
        self.inorder(self.root)
        print(" " + " ".join(map(str, self.ino)))
        self.preorder(self.root)
        print(" " + " ".join(map(str, self.preo)))


if __name__ == "__main__":
    n = int(input())
    bst = BST()

    for _ in range(n):
        com, *val = input().split()
        if com == "insert":
            bst.insert(Node(int(val[0])))
        elif com == "print":
            bst.print()
