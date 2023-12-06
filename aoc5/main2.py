import re

input = open("input.txt", 'r')

d = dict()

l_array = []
for line in input:
    if line == "\n":
        continue
    l_array.append(line.removesuffix("\n"))

names = [[]]
seed_ranges = []
i = 0
while i < len(l_array):
    sp = l_array[i].split(":")
    if sp[0] == "seeds":
        seed_ranges = re.findall(r"\d+ \d+", sp[1])
        i += 1
        continue
    name = sp[0].removesuffix(" map")
    names.append([name.split("-")[0], name.split("-")[2]])
    while not (i + 1 == len(l_array) or re.match(r".* map", l_array[i + 1].split(":")[0])):
        i += 1
        if not name in d:
            d[name] = [[int(i) for i in re.findall(r"\d+", l_array[i])]]
        else:
            d[name].append([int(i) for i in re.findall(r"\d+", l_array[i])])
    i += 1

positions = []
for seed_range in seed_ranges:
    start = int(seed_range.split(" ")[0])
    finish = int(seed_range.split(" ")[1])+start
    r = [(start, finish)]
    A = []
    for mapping in d["seed-to-soil"]:
        NR = []
        dest = mapping[0]
        src = mapping[1]
        s = mapping[2]

        src_end = src+s

        while r:
            (st,ed) = r.pop()

            before = (st, min(ed, src))
            inter = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)

            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                A.append((inter[0] - src + dest, inter[1] - src + dest))
            if after[1] > after[0]:
                NR.append(after)
        r = NR
    r = A+r
    for target in names[2:]:
        fr = target[0]
        to = target[1]
        A = []
        for mapping in d["{}-to-{}".format(fr, to)]:
            NR = []
            dest = mapping[0]
            src = mapping[1]
            s = mapping[2]

            src_end = src + s

            while r:
                (st, ed) = r.pop()

                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)

                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            r = NR
        r = A + r
    positions.append(min(r)[0])
print(min(positions))
