from collections import deque

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    q = int(input())
    d = deque()
    for _ in range(q):
        c = list(map(int, input().split()))
        if c[0] == 0 and c[1] == 0:
            d.appendleft(c[2])
        elif c[0] == 0 and c[1] == 1:
            d.append(c[2])
        elif c[0] == 2 and c[1] == 0:
            d.popleft()
        elif c[0] == 2 and c[1] == 1:
            d.pop()
        elif c[0] == 1:
            print(d[c[1]])
