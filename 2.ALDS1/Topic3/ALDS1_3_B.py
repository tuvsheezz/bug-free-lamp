from collections import deque
dq = deque()

n, q = map(int, input().split())

for i in range(n):
    name, time = input().split()
    dq.append([name, int(time)])

total_time = 0

while len(dq) > 0:
    name, time = dq.popleft()
    if time <= q:
        total_time += time
        print(name, total_time)
    else:
        total_time += q
        dq.append([name, time - q])
