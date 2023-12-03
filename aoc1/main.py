import regex as re

input = open("input.txt", "r")

sum = 0
for l in input:
    line = l
    out = ""
    for match in re.finditer(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)", line, overlapped=True):
        if match.group() == "one" or match.group() == "1":
            out += "1"
        elif match.group() == "two" or match.group() == "2":
            out += "2"
        elif match.group() == "three" or match.group() == "3":
            out += "3"
        elif match.group() == "four" or match.group() == "4":
            out += "4"
        elif match.group() == "five" or match.group() == "5":
            out += "5"
        elif match.group() == "six" or match.group() == "6":
            out += "6"
        elif match.group() == "seven" or match.group() == "7":
            out += "7"
        elif match.group() == "eight" or match.group() == "8":
            out += "8"
        elif match.group() == "nine" or match.group() == "9":
            out += "9"

    val = int("%s%s" % (out[0], out[-1]))
    sum += val
print(sum)
