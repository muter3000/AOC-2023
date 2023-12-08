from collections import defaultdict


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

print(translated_graph)

pos = 'AAA'
i = 0
while pos != 'ZZZ':
    i+=1
    pos = translated_graph[pos]

print(i*len(seq))