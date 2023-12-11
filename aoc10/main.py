import re
from enum import Enum

inp = open("input.txt", "r")

# y down x right
map2d = [[i for i in l.removesuffix("\n")] for l in inp]


class Before(Enum):
    North = 0
    West = 1
    South = 2
    East = 3


def findSConnection(x, y):
    _n = []
    if x + 1 < len(map2d[y]):
        _next = map2d[y][x + 1]
        if _next == "-" or _next == "J" or _next == "7":
            _n.append((x + 1, y, Before.West))
    if x - 1 >= 0:
        _next = map2d[y][x - 1]
        if _next == "-" or _next == "L" or _next == "F":
            _n.append((x - 1, y, Before.East))
    if y - 1 >= 0:
        _next = map2d[y - 1][x]
        if _next == "|" or _next == "F" or _next == "7":
            _n.append((x, y - 1, Before.South))
    if len(_n) == 1:
        _n.append((x, y + 1, Before.North))
    return _n


def nextSymbol(x: int, y: int, b: Before):
    s = map2d[y][x]
    if s == "-":
        if b == Before.West:
            return x + 1, y, Before.West
        return x - 1, y, Before.East
    elif s == "|":
        if b == Before.South:
            return x, y - 1, Before.South
        return x, y + 1, Before.North
    elif s == "J":
        if b == Before.North:
            return x - 1, y, Before.East
        return x, y - 1, Before.South
    elif s == "7":
        if b == Before.South:
            return x - 1, y, Before.East
        return x, y + 1, Before.North
    elif s == "F":
        if b == Before.South:
            return x + 1, y, Before.West
        return x, y + 1, Before.North
    elif s == "L":
        if b == Before.North:
            return x + 1, y, Before.West
        return x, y - 1, Before.South


out = [[0 for i in y] for y in map2d]


def findMaxDistance(_x1, _y1, _b1, _x2, _y2, _b2):
    s = 0
    while not (_x1 == _x2 and _y1 == _y2):
        s += 1
        out[_y1][_x1] = 1
        out[_y2][_x2] = 1

        _x1, _y1, _b1 = nextSymbol(_x1, _y1, _b1)
        _x2, _y2, _b2 = nextSymbol(_x2, _y2, _b2)
    out[_y1][_x1] = 1
    out[_y2][_x2] = 1
    return s + 1


sx = 0
sy = 0

for y, l in enumerate(map2d):
    for x, _ in enumerate(l):
        if map2d[y][x] == "S":
            sx = x
            sy = y
            break

scon = findSConnection(sx, sy)
x1, y1, b1 = scon[0]
x2, y2, b2 = scon[1]

out[sy][sx] = 1

print(findMaxDistance(x1, y1, b1, x2, y2, b2))


def shootRay(a, b, val):
    if val == 1:
        return 0
    _x = a + 1
    _y = b + 1
    s = 0
    while _x < len(map2d[0]) and _y < len(map2d):
        if out[_y][_x] == 1 and re.match(r"[-|JF]", map2d[_y][_x]):
            s += 1
        _x += 1
        _y += 1

    return int((s % 2) == 1)


insides = [[shootRay(x, y, val) for x, val in enumerate(ys)] for y, ys in enumerate(out)]
s = 0
for a in insides:
    for x in a:
        s += x

print(s)
