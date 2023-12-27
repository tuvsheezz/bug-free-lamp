w, h, x, y, r = map(int, input().split())
xmin = x - r
xmax = x + r
ymin = y - r
ymax = y + r

if 0 <= xmin and xmax <= w and 0 <= ymin and ymax <= h:
    print("Yes")
else:
    print("No")
