inp = open('input.txt','r')

import re

lines = [[int(x) for x in re.findall(r"-{0,1}\d+",i)] for i in inp]


def extra(ys):
    n = ys
    s = 0
    while not all([x==0 for x in n]):
        s += n[-1]
        n = [n[i+1]-x for i,x in enumerate(n[:len(n)-1])]
    return s

ext = [extra(y) for y in lines]
ext2 = [extra(y[::-1]) for y in lines]

print(sum(ext))
print(sum(ext2))

