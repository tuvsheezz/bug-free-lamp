class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i


if __name__ == "__main__":
    n, q = map(int, input().split())
    bit = BinaryIndexedTree(n)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com:
            print(bit.sum(y) - bit.sum(x - 1))
        else:
            bit.add(x, y)

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B
