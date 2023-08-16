from collections import deque
import sys

n = int(input())
q = deque()
for com in sys.stdin.readlines():
    if com[0] == "i":
        x = int(com[7:])
        q.appendleft(x)

    elif com[0] == "d":
        if com[6] == "F":
            q.popleft()

        elif com[6] == "L":
            q.pop()

        else:
            x = int(com[7:])
            try:
                q.remove(x)
            except:
                pass

print(*q)
