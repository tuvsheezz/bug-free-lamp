from sys import stdin
from collections import deque

f_i = stdin
q = f_i.readline()
d = 0


L = deque()

for l in f_i:
    if l[0] == "0":
        L.append(l[2:])
    elif l[0] == "1":
        r = int(l[2:])
        L.rotate(r)
        d -= r
    else:
        L.pop()
L.rotate(d)
L.reverse()
print("".join(L), end="")
