class RollingHash:
    def __init__(self, s: str) -> None:
        self.base: int = 31
        self.mod: int = (10**9) + 9
        self.pow: list[int] = [1] * (len(s) + 1)
        self.h: list[int] = [0] * (len(s) + 1)

        for i in range(len(s)):
            self.h[i + 1] = (self.h[i] * self.base + ord(s[i]) - ord("a")) % self.mod

        for i in range(len(s)):
            self.pow[i + 1] = self.pow[i] * self.base % self.mod

    def get(self, le: int, ri: int) -> int:
        return (self.h[ri] - self.h[le] * self.pow[ri - le]) % self.mod


if __name__ == "__main__":
    s: str = input()
    t: str = input()

    rs = RollingHash(s)
    rt = RollingHash(t)

    for i in range(len(s) - len(t) + 1):
        if rs.get(i, i + len(t)) == rt.get(0, len(t)):
            print(i)
