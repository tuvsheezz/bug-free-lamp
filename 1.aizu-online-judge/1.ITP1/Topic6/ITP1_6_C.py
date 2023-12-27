rooms = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
for _ in range(int(input())):
    b, f, r, t = map(int, input().split())
    rooms[b - 1][f - 1][r - 1] += t
for i in range(4):
    if not i == 0:
        print("#" * 20)
    for j in range(3):
        print("", *rooms[i][j])
