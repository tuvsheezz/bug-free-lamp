while True:
    s = input()
    if s == "-":
        break
    m = int(input())
    index = 0
    for _ in range(m):
        h = int(input())
        index = (index + h) % len(s)
    print(s[index:] + s[:index])
