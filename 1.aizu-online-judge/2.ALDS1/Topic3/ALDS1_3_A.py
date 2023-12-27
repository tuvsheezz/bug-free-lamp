from collections import deque

dq = deque()
for x in list(input().split()):
    if x.isdigit():
        dq.append(x)
    else:
        a = dq.pop()
        b = dq.pop()
        dq.append(str(eval(b + x + a)))
print(dq.pop())
