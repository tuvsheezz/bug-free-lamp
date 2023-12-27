s = input()
n = int(input())
for i in range(n):
    c = input().split()
    if c[0] == "print":
        print(s[int(c[1]) : int(c[2]) + 1])
    elif c[0] == "reverse":
        s = s[: int(c[1])] + s[int(c[1]) : int(c[2]) + 1][::-1] + s[int(c[2]) + 1 :]
    elif c[0] == "replace":
        s = s[: int(c[1])] + c[3] + s[int(c[2]) + 1 :]
