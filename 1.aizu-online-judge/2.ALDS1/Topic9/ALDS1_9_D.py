def maxHeapify(A, i, size):
    le = i * 2
    ri = i * 2 + 1
    largest = i
    if le <= size and A[le] > A[i]:
        largest = le

    if ri <= size and A[ri] > A[largest]:
        largest = ri

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, size)


def heapSort(A):
    size = len(A) - 1
    for i in range(size // 2, 0, -1):
        maxHeapify(A, i, size)

    while size >= 2:
        A[1], A[size] = A[size], A[1]
        size -= 1
        maxHeapify(A, 1, size)


input()
A = [0] + list(map(int, input().split()))
heapSort(A)
print(" " + " ".join(map(str, A[1:])))
