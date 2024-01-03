class PriorityQueue:
    def __init__(self):
        self.A = [0]
        self.size = 0

    def maxHeapify(self, i):
        le = i * 2
        ri = i * 2 + 1
        largest = i

        if le <= self.size and self.A[le] > self.A[i]:
            largest = le

        if ri <= self.size and self.A[ri] > self.A[largest]:
            largest = ri

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.maxHeapify(largest)

    def insert(self, k):
        self.size += 1
        self.A.append(-float("inf"))
        self.heapIncreaseKey(self.size, k)

    def heapIncreaseKey(self, i, k):
        if k < self.A[i]:
            return

        self.A[i] = k
        while i > 1 and self.A[i // 2] < self.A[i]:
            self.A[i // 2], self.A[i] = self.A[i], self.A[i // 2]
            i //= 2

    def top(self):
        if self.isEmpty():
            return None

        mx = self.A[1]
        self.A[1] = self.A[self.size]
        self.A.pop()
        self.size -= 1
        self.maxHeapify(1)
        return mx

    def isEmpty(self):
        return self.size == 1


if __name__ == "__main__":
    pq = PriorityQueue()
    while True:
        com, *v = input().split()
        if com == "end":
            break
        elif com == "insert":
            pq.insert(int(v[0]))
        elif com == "extract":
            print(pq.top())
