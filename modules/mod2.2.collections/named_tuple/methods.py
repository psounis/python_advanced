from collections import namedtuple

Point = namedtuple("Point", "x y")

p = Point(1.1, 2.8)
print(p._make([1, 1]))
print(p._asdict())
print(p._replace(x=3.3))
print(p._fields)
