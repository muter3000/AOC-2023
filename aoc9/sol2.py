inp = open('input.txt','r')

from scipy import interpolate
import re

lines = [[int(x) for x in re.findall(r"-{0,1}\d+",i)] for i in inp]

ext = [interpolate.krogh_interpolate(range(0, len(y)), y, len(y)) for y in lines]
ext2 = [interpolate.krogh_interpolate(range(0, len(y)), y[::-1], len(y)) for y in lines]

print(round(sum(ext)))
print(round(sum(ext2)))
