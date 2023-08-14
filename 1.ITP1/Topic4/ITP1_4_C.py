while True:
    a = input().split()
    x, y = int(a[0]), int(a[2])
    op = a[1]
    if op == "?":
        break

    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x // y)
