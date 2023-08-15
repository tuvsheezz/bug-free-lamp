import math
a = list(map(float, input().split()))
print('{:.010f}'.format(math.dist(a[:2], a[2:])))
