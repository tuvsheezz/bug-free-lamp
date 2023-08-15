while True:
    s = input()
    if s == '0':
        break
    print(sum(map(int, s)))
