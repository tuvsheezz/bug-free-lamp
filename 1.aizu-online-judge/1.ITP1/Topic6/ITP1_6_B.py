mark = ["S", "H", "C", "D"]
cards = [[False for _ in range(14)] for _ in range(4)]

for _ in range(int(input())):
    m, num = input().split()
    cards[mark.index(m)][int(num)] = True

for i in range(4):
    for j in range(1, 14):
        if not cards[i][j]:
            print(mark[i], j)
