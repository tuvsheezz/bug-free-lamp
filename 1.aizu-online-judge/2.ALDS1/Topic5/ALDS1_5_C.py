import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance(self, point=None):
        if not point:
            point = Point()
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


def koch(_p1, _p2, depth):
    if depth == 0:
        return
    else:
        s = Point()
        t = Point()
        u = Point()
        rad = math.radians(60)
        s.x = (2 * _p1.x + _p2.x) / 3
        s.y = (2 * _p1.y + _p2.y) / 3
        t.x = (_p1.x + 2 * _p2.x) / 3
        t.y = (_p1.y + 2 * _p2.y) / 3
        u.x = (t.x - s.x) * math.cos(rad) - (t.y - s.y) * math.sin(rad) + s.x
        u.y = (t.x - s.x) * math.sin(rad) + (t.y - s.y) * math.cos(rad) + s.y
        koch(_p1, s, depth - 1)
        print(s.x, s.y)
        koch(s, u, depth - 1)
        print(u.x, u.y)
        koch(u, t, depth - 1)
        print(t.x, t.y)
        koch(t, _p2, depth - 1)


if __name__ == "__main__":
    n = int(input())
    p1 = Point(0.0, 0.0)
    p2 = Point(100.0, 0.0)
    print(p1.x, p1.y)
    koch(p1, p2, n)
    print(p2.x, p2.y)
