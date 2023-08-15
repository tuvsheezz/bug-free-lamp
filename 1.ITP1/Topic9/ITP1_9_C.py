sc1, sc2 = 0, 0

for _ in range(int(input())):
    s, t = input().split()
    if s == t:
        sc1 += 1
        sc2 += 1
    elif s > t:
        sc1 += 3
    else:
        sc2 += 3
print(sc1, sc2)
