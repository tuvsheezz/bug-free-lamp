n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print("node {}: key = {}, ".format(i + 1, a[i]), end="")
    if i > 0:
        print("parent key = {}, ".format(a[(i - 1) // 2]), end="")
    if i * 2 + 1 < n:
        print("left key = {}, ".format(a[i * 2 + 1]), end="")
    if i * 2 + 2 < n:
        print("right key = {}, ".format(a[i * 2 + 2]), end="")
    print()
