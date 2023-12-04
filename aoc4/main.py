import regex

input = open("input.txt", 'r')

array3d = []

for line in input:
    sp = line.split(":")
    nums = sp[1].split("|")
    nums1 = regex.findall(r'\d+', nums[1])
    nums0 = regex.findall(r'\d+', nums[0])
    card = [[int(i) for i in nums0], [int(i) for i in nums1]]
    array3d.append(card)

r_winds = [0 for i in array3d]
for i, round in enumerate(array3d):
    wins = set(round[0]).intersection(set(round[1]))
    r_winds[i] = len(wins)

cards = [1 for i in array3d]
for i, win in enumerate(r_winds):
    for x in range(1, win+1):
        cards[x + i] += cards[i]

print(sum(cards))
