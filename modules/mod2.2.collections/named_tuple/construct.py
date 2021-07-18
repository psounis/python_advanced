from collections import namedtuple

Point = namedtuple("Point", "x y")

p = Point(1.4, 2.8)
print(p[0], p[1])
print(p.x, p.y)