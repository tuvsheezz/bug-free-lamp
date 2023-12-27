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
    n = int(input())
    a = list(map(int, input().split()))

    dic = {b: i for i, b in enumerate(sorted(a), 1)}

    bit = BinaryIndexedTree(n)
    ans = 0

    for i, a in enumerate(a):
        ans += i - bit.sum(dic[a])
        bit.add(dic[a], 1)
    print(ans)
