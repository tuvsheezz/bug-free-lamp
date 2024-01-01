import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.ino = list()
        self.preo = list()

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

    def find(self, root, k):
        if root is None:
            return None
        if root.data == k:
            return root
        elif k < root.data:
            return self.find(root.left, k)
        else:
            return self.find(root.right, k)

    def delete(self, k):
        node = self.find(self.root, k)
        if node is None:
            return

        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            elif node.parent.data < node.data:
                node.parent.right = None
                node.parent = None
            else:
                node.parent.left = None
                node.parent = None
        elif node.right is None:
            if node.parent is None:
                node.left.parent = None
                self.root = node.left
                node.left = None
            elif node.parent.data < node.data:
                node.parent.right, node.left.parent = node.left, node.parent
            else:
                node.parent.left, node.left.parent = node.left, node.parent
        elif node.left is None:
            if node.parent is None:
                node.right.parent = None
                self.root = node.right
                node.right = None
            elif node.parent.data < node.data:
                node.parent.right, node.right.parent = node.right, node.parent
            else:
                node.parent.left, node.right.parent = node.right, node.parent
        else:
            self.ino = list()
            self.inorder(self.root)
            ind = self.ino.index(node.data)
            new_data = self.ino[ind + 1]
            self.delete(new_data)
            node.data = new_data

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
        elif com == "find":
            if bst.find(bst.root, int(val[0])):
                print("yes")
            else:
                print("no")
        elif com == "delete":
            bst.delete(int(val[0]))
