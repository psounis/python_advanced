# official docs example: https://docs.python.org/3/library/enum.html
from enum import Flag, auto


class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    WHITE = RED|GREEN|BLUE


for item in Color:
    print(item, item.value)