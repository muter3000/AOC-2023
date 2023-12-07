from collections import Counter

inp = open("input.txt", 'r')

lines = [i for i in inp]


# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
def replaceType(s: str):
    s = s.replace('A', 'Z')
    s = s.replace('K', 'Y')
    s = s.replace('Q', 'X')
    s = s.replace('J', 'W')
    s = s.replace('T', 'V')
    s = s.replace('9', 'U')
    s = s.replace('8', 'T')
    s = s.replace('7', 'S')
    s = s.replace('6', 'R')
    s = s.replace('5', 'Q')
    s = s.replace('4', 'P')
    s = s.replace('3', 'O')
    s = s.replace('2', 'A')

    return s


hands = [(i.split(" ")[0], int(i.split(" ")[1].removesuffix("\n"))) for i in lines]


# type, hand, bid
def get_type(hand):
    result = Counter(hand)

    if max(result.values()) == 5:
        return 8
    if max(result.values()) == 4:
        return 7
    if max(result.values()) == 3:
        if list(result.values()).count(2) == 1:
            return 6
        else:
            return 5
    if (max(result.values())) == 2:
        if list(result.values()).count(2) == 2:
            return 3
        else:
            return 2
    return 1


typed_hands = [(get_type(hand), replaceType(hand), hand, bid) for (hand, bid) in hands]
sortedHand = sorted(typed_hands, key=lambda x: (x[0], x[1]))

s = 0
for i, (_, _, _, bid) in enumerate(sortedHand):
    s += (i + 1) * bid

print(s)

open("out.txt", 'w').write(str(sortedHand))
