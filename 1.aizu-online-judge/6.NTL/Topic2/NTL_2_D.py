a, b = map(int, input().split())
c = abs(a) // abs(b)

if a * b < 0:
    c *= -1

print(c)
