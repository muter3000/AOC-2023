import re

input = open("input.txt", 'r')

d = dict()

l_array = []
for line in input:
    if line == "\n":
        continue
    l_array.append(line.removesuffix("\n"))

names = [[]]
seeds = []
i = 0
while i < len(l_array):
    sp = l_array[i].split(":")
    if sp[0] == "seeds":
        seeds = [int(i) for i in re.findall(r"\d+", sp[1])]
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
for seed in seeds:
    pos = seed
    for mapping in d["seed-to-soil"]:
        if mapping[1] <= seed < mapping[1] + mapping[2]:
            pos = pos - mapping[1] + mapping[0]
            break
    for target in names[2:]:
        fr = target[0]
        to = target[1]
        for mapping in d["{}-to-{}".format(fr, to)]:
            if mapping[1] <= pos < mapping[1] + mapping[2]:
                pos = pos - mapping[1] + mapping[0]
                break
    positions.append(pos)

print(min(positions))
