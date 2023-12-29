class MergeSort:
    import sys

    sys.setrecursionlimit(10**9)

    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.sentinel = float("inf")
        self.l = [0] * (n // 2 + 2)
        self.r = [0] * (n // 2 + 2)
        self.comp_count = 0

    def merge(self, left, mid, right):
        n1, n2 = mid - left, right - mid
        for i in range(n1):
            self.l[i] = self.arr[left + i]
        for i in range(n2):
            self.r[i] = self.arr[mid + i]

        self.l[n1] = self.sentinel
        self.r[n2] = self.sentinel

        i, j = 0, 0

        for k in range(left, right):
            self.comp_count += 1
            if self.l[i] <= self.r[j]:
                self.arr[k] = self.l[i]
                i += 1
            else:
                self.arr[k] = self.r[j]
                j += 1

    def sort(self, left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            self.sort(left, mid)
            self.sort(mid, right)
            self.merge(left, mid, right)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    ms = MergeSort(arr, n)
    ms.sort(0, n)
    print(*ms.arr)
    print(ms.comp_count)
