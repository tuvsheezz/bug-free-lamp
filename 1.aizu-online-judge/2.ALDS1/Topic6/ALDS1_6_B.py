def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    i = partition(a, 0, n - 1)
    print(*a[:i], sep=" ", end=" ")
    print("[{}]".format(a[i]), end=" ")
    print(*a[i + 1 :], sep=" ")
