class SortAlgorithm:
    def __init__(self):
        pass

    def bubble_sort(self, a):
        n = len(a)
        swap_count = 0
        for i in range(n):
            for j in range(n - 1, i, -1):
                if a[j][1] < a[j - 1][1]:
                    a[j - 1], a[j] = a[j], a[j - 1]
                    swap_count += 1
        return swap_count

    def selection_sort(self, a):
        n = len(a)
        swap_count = 0
        for i in range(n):
            mini = i
            for j in range(i, n):
                if a[j][1] < a[mini][1]:
                    mini = j
            if i != mini:
                swap_count += 1
            a[i], a[mini] = a[mini], a[i]
        return swap_count


if __name__ == "__main__":
    _ = int(input())
    sa = SortAlgorithm()
    a = list(input().split())
    b = a.copy()
    sa.bubble_sort(a)
    print(*a)
    print("Stable")
    sa.selection_sort(b)
    print(*b)
    print("Stable" if a == b else "Not stable")
