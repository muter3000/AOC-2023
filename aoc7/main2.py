from collections import Counter

inp = open("input.txt", 'r')

lines = [i for i in inp]


# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
def replaceType(s: str):
    s = s.replace('A', 'Z')
    s = s.replace('K', 'Y')
    s = s.replace('Q', 'X')
    s = s.replace('J', 'A')
    s = s.replace('T', 'V')
    s = s.replace('9', 'U')
    s = s.replace('8', 'T')
    s = s.replace('7', 'S')
    s = s.replace('6', 'R')
    s = s.replace('5', 'Q')
    s = s.replace('4', 'P')
    s = s.replace('3', 'O')
    s = s.replace('2', 'B')

    return s


hands = [(i.split(" ")[0], int(i.split(" ")[1].removesuffix("\n"))) for i in lines]


# type, hand, bid
def get_type(hand):
    result = Counter(hand)

    if max(result.values()) == 5:
        return 7
    # XXXXJ JJJJX
    elif max(result.values()) == 4:
        if result['J'] >= 1:
            return 7
        else:
            return 6
    # XXXJY JJJYX XXXJY XXXJJ
    elif max(result.values()) == 3:
        if list(result.values()).count(2) == 1:
            if result['J'] >= 2:
                return 7
            return 5
        else:
            if result['J'] >= 1:
                return 6
            return 4
    # XXJJY XXYYJ JJXYZ JXXYZ
    elif (max(result.values())) == 2:
        if list(result.values()).count(2) == 2:
            if result['J'] == 2:
                return 6
            if result['J'] == 1:
                return 5
            return 3
        else:
            if result['J'] == 2 or result['J'] == 1:
                return 4
            return 2

    if result['J'] == 1:
        return 2
    return 1


typed_hands = [(get_type(hand), replaceType(hand), hand, bid) for (hand, bid) in hands]
sortedHand = sorted(typed_hands, key=lambda x: (x[0], x[1]))

s = 0
for i, (_, _, _, bid) in enumerate(sortedHand):
    s += (i + 1) * bid

print(s)

open("out.txt", 'w').write(str(sortedHand))
