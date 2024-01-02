import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, key, pri):
        self.key = key
        self.priority = pri
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def rightRotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def leftRotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, t, key, priority):
        if t is None:
            return Node(key, priority)

        if key == t.key:
            return t

        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if t.priority < t.left.priority:
                t = self.rightRotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if t.priority < t.right.priority:
                t = self.leftRotate(t)

        return t

    def delete(self, t, key):
        if t is None:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self._delete(t, key)
        return t

    def _delete(self, t, key):
        if t.left is None and t.right is None:
            return None
        elif t.left is None:
            t = self.leftRotate(t)
        elif t.right is None:
            t = self.rightRotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.rightRotate(t)
            else:
                t = self.leftRotate(t)
        return self.delete(t, key)

    def find(self, t, key):
        if t is None:
            return False
        if key == t.key:
            return True
        if key < t.key:
            return self.find(t.left, key)
        else:
            return self.find(t.right, key)

    def print_inorder(self, t):
        if t is None:
            return
        self.print_inorder(t.left)
        print(" ", end="")
        print(t.key, end="")
        self.print_inorder(t.right)

    def print_preorder(self, t):
        if t is None:
            return
        print(" ", end="")
        print(t.key, end="")
        self.print_preorder(t.left)
        self.print_preorder(t.right)

    def print(self):
        self.print_inorder(self.root)
        print()
        self.print_preorder(self.root)
        print()


if __name__ == "__main__":
    trp = Treap()
    n = int(input())

    for _ in range(n):
        com, *val = input().split()
        if com == "insert":
            trp.root = trp.insert(trp.root, int(val[0]), int(val[1]))
        elif com == "print":
            trp.print()
        elif com == "find":
            if trp.find(trp.root, int(val[0])):
                print("yes")
            else:
                print("no")
        elif com == "delete":
            trp.root = trp.delete(trp.root, int(val[0]))
