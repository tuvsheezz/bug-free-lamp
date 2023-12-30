# Counting sort can be used for sorting elements
# in an array which each of the n input elements
# is an integer in the range 0 to k.


def count_sort(a):
    k = max(a)
    c = [0] * (k + 1)
    for x in a:
        c[x] += 1
    ind = 0
    for i in range(0, k + 1):
        for _ in range(0, c[i]):
            a[ind] = i
            ind += 1


if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    count_sort(a)
    print(*a)
