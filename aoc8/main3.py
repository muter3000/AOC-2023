import numpy as np
from math import lcm
import re


inp = open("input.txt",'r')

lines = [line for line in inp]

seq = lines[0].removesuffix("\n")

graph = dict([(i[:3],(i[7:10],i[12:15])) for i in lines[2:]])

translated_seq = seq.translate(str.maketrans("LR","01"))

def translate(start:str, seq:str, m:dict):
    pos = start
    for c in seq:
        pos = m[pos][int(c)]
    return pos

translated_graph = dict([(i[:3],translate(i[:3],translated_seq,graph)) for i in lines[2:]])

#print(translated_graph)

joined = ";".join(list(translated_graph.keys()))

def isEnd(current):
    return current[2]=='Z'

positions = re.findall('[A-Z0-9][A-Z0-9]A',joined)
x = 0

def findNumberOfSteps(start,m):
    a = 0
    c = start
    while not isEnd(c):
        a += 1
        c = m[c]
    return a

numOfSteps = [findNumberOfSteps(s, translated_graph) for s in positions]

print(np.lcm.reduce(numOfSteps)*len(seq))