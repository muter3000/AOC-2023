import re

input = open("input.txt", 'r')

array2D = []

for line in input.readlines():
    array2D.append(line.replace("\n", ""))

sum = 0

for i, line in enumerate(array2D):
    for match in re.finditer(r'\d+', line):
        neighbours_s = []
        symbols = []
        l_index = match.span()[0] - 1
        r_index = match.span()[1] + 1
        if match.span()[0] == 0:
            l_index += 1
        if match.span()[1] == len(line):
            r_index -= 1
        if i != 0:
            neighbours_s.append(array2D[i - 1][l_index:r_index])
        if i != len(array2D) - 1:
            neighbours_s.append(array2D[i + 1][l_index:r_index])
        if l_index != 0:
            neighbours_s.append(line[l_index])
        if r_index != len(line):
            neighbours_s.append(line[r_index-1])
        for el in neighbours_s:
            for c in el:
                symbols.append(c)
        symbols = set(symbols).difference('.')
        if len(symbols) > 0:
            sum += int(match.group())
print(sum)
