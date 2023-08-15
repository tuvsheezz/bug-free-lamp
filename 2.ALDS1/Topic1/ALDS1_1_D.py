mn = 10**18
p = -10**18
for i in range(int(input())):
    r = int(input())
    if i:
        p = max(p, r - mn)
    mn = min(mn, r)
print(p)
