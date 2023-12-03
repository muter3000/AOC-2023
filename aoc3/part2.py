import re

input = open("input.txt", 'r')

array2D = []

for line in input.readlines():
    array2D.append(line.replace("\n", ""))

sum = 0
for i, line in enumerate(array2D):
    for possible_gear in re.finditer("\*", line):
        nums = []
        if i != 0:
            for possible_num in re.finditer(r"\d+", array2D[i - 1]):
                if possible_num.span(0)[1] >= possible_gear.span()[0] >= possible_num.span()[0] - 1:
                    nums.append(possible_num.group())
        if i != len(array2D) - 1:
            for possible_num in re.finditer(r"\d+", array2D[i + 1]):
                if possible_num.span(0)[1] >= possible_gear.span()[0] >= possible_num.span()[0] - 1:
                    nums.append(possible_num.group())
        for possible_num in re.finditer(r"\d+", line):
            if possible_num.span()[0] == possible_gear.span()[1]:
                nums.append(possible_num.group())
            if possible_num.span()[1] == possible_gear.span()[0]:
                nums.append(possible_num.group())
        if len(nums) == 2:
            sum += int(nums[0]) * int(nums[1])
print(sum)
