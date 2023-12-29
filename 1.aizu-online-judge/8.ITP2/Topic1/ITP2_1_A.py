a = list()
for _ in range(int(input())):
    c = list(map(int, input().split()))
    if c[0] == 0:
        a.append(c[1])
    elif c[0] == 1:
        print(a[c[1]])
    else:
        a.pop()
