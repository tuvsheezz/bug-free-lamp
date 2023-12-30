class Item:
    def __init__(self):
        self.key = None
        self.value = None
        self.index = None


def partition(a, p, r):
    x = a[r].value
    i = p - 1
    for j in range(p, r):
        if a[j].value <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


if __name__ == "__main__":
    n = int(input())
    a = [Item() for _ in range(n)]
    for i in range(n):
        a[i].key, a[i].value = input().split()
        a[i].value = int(a[i].value)
        a[i].index = i
    quicksort(a, 0, n - 1)
    stable = True
    for i in range(1, n):
        if a[i - 1].value == a[i].value and a[i - 1].index > a[i].index:
            stable = False
            break
    if stable:
        print("Stable")
    else:
        print("Not stable")
    for i in range(n):
        print(a[i].key, a[i].value)
