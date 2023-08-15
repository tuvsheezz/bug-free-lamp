import math
a, b, angle = map(float, input().split())
s = a * b * math.sin(math.radians(angle)) / 2
l = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b *
                      math.cos(math.radians(angle)))
h = b * math.sin(math.radians(angle))

print(*[s, l, h], sep='\n')
