while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(float, input().split()))
    avg = sum(s) / n
    print((sum([(i - avg) ** 2 for i in s]) / n) ** 0.5)
