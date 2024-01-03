def maxHeapify(A, i):
    le = i * 2
    ri = i * 2 + 1
    largest = i
    if le < len(A) and A[le] > A[i]:
        largest = le

    if ri < len(A) and A[ri] > A[largest]:
        largest = ri

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)


def buildMaxHeap(A):
    for i in range(len(A) // 2, 0, -1):
        maxHeapify(A, i)


input()
A = [0] + list(map(int, input().split()))
buildMaxHeap(A)
print(" " + " ".join(map(str, A[1:])))
