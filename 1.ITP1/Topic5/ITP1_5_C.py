c = '#.' * 151
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    for i in range(h):
        if i % 2 == 0:
            print(c[0:w])
        else:
            print(c[1:w + 1])
    print()
