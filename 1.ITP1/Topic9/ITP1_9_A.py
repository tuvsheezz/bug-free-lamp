s = input().lower()
ans = 0
while True:
    p = input()
    if p == 'END_OF_TEXT':
        break
    ans += p.lower().split().count(s)
print(ans)
