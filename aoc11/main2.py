from itertools import combinations

inp = open("input.txt", 'r')

map2d: list[list[str]] = [[i for i in line.removesuffix("\n")] for line in inp]

emptyRows = []
s = 0
for i, l in enumerate(map2d):
    if all([c == "." for c in l]):
        emptyRows.append(i)

transposed = list(map(list, zip(*map2d)))

emptyColumns = []
s = 0
for i, l in enumerate(transposed):
    if all([c == "." for c in l]):
        emptyColumns.append(i)

gal = []
for y, l in enumerate(map2d):
    for x, item in enumerate(l):
        if item == "#":
            gal.append((x, y))

res = list(combinations(gal, 2))


def calculateDistance(p1, p2, _rows, _cols, age):
    x1, y1 = p1
    x2, y2 = p2
    s = abs(x1 - x2) + abs(y1 - y2)
    for e in _rows:
        if y1 < e < y2 or y2 < e < y1:
            s += age

    for e in _cols:
        if x1 < e < x2 or x2 < e < x1:
            s += age
    return s


distances = [calculateDistance(p1, p2, emptyRows, emptyColumns, 1000000-1) for (p1, p2) in res]

print(sum(distances))
