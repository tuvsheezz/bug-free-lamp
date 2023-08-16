s = input()
a = []
down = []
for i, line in enumerate(s):
    if line == "\\":
        down.append(i)
    elif line == "/" and down:
        j = down.pop()
        a_tmp = i-j
        while a and a[-1][0] > j:
            a_tmp += a.pop()[1]
        a.append([j, a_tmp])

print(sum([s for i, s in a]))
print(len(a), *[s for i, s in a])
