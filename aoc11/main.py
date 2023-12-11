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

expandedMap = map2d
for x, i in enumerate(emptyRows):
    toInsert: list[str] = ["." for f in map2d[0]]
    expandedMap.insert(i + x, toInsert)

for a, _ in enumerate(expandedMap):
    for x, i in enumerate(emptyColumns):
        expandedMap[a].insert(i + x, ".")

gal = []
for y, l in enumerate(expandedMap):
    for x, item in enumerate(l):
        if item == "#":
            gal.append((x, y))

res = list(combinations(gal, 2))

distances = [abs(x1-x2)+abs(y1-y2) for ((x1,y1),(x2,y2)) in res]
print(sum(distances))
