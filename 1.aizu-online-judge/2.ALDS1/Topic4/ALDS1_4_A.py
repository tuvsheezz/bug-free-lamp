s = dict()
ans = 0
input()
for i in map(int, input().split()):
    s[i] = 1

input()
for i in map(int, input().split()):
    if i in s:
        ans += 1
print(ans)
