x = int(input())
h = x // 3600
x %= 3600
m = x // 60
s = x % 60
print("%d:%d:%d" % (h, m, s))
