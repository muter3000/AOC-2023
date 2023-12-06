import math
import re
from math import sqrt

input = open("input2.txt", 'r')

lines = [line for line in input]
t = [int(i) for i in re.findall(r"\d+", lines[0])]
d = [int(i) for i in re.findall(r"\d+", lines[1])]
races = list(zip(t, d))


# d = (t-t_t)*t_t
# t-t_t = d/t_t
# t_t = t-d/t_t
# t_t^2 - t*t_t + d = 0
# delta = t^2 - 4*d
# a1 = (t-sqrt(delta))/2
# a2 = (t+sqrt(delta))/2

def calculate(d, t):
    delta = t * t - 4 * d
    return int((t - sqrt(delta)) / 2)+1, math.ceil(((t + sqrt(delta)) / 2))


trigger_times = [calculate(d, t) for (t, d) in races]
num = [r-l for (l, r) in trigger_times]

print(math.prod(num))
