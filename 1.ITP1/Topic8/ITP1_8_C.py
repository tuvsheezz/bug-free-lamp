alf = [0] * 26
while True:
    try:
        str = input().lower()
    except:
        break
    for c in str:
        if c.isalpha():
            alf[ord(c)-ord("a")] += 1

for i in range(26):
    print(chr(97 + i), ":", alf[i])
