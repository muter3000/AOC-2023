import re

red = 12
green = 13
blue = 14

input = open("input.txt", "r")
id_sum = 0
power = 0

for line in input:
    sp = re.split(":", line)
    turns = re.split(";", sp[1])
    t_green = 0
    t_blue = 0
    t_red = 0
    impossible = False

    min_red = 0
    min_blue = 0
    min_green = 0
    for turn in turns:
        t_green = 0
        t_blue = 0
        t_red = 0

        t_green_s = re.finditer(r"\d+ green", turn)
        for s in t_green_s:
            s_split = re.split(r" ", s.group())
            t_green += int(s_split[0])

        t_blue_s = re.finditer(r"\d+ blue", turn)
        for s in t_blue_s:
            s_split = re.split(r" ", s.group())
            t_blue += int(s_split[0])

        t_red_s = re.finditer(r"\d+ red", turn)
        for s in t_red_s:
            s_split = re.split(r" ", s.group())
            t_red += int(s_split[0])
        if (t_red > red or t_blue > blue or t_green > green):
            impossible = True
        if min_red < t_red:
            min_red = t_red
        if min_green < t_green:
            min_green = t_green
        if min_blue < t_blue:
            min_blue = t_blue
    if not impossible:
        id_sum += int(sp[0][5:])
    power += (min_blue*min_green*min_red)
print(power)
