import re
with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)

# Part 1
matches = []
for line in lines:
    #print(line)
    line_matches = re.findall(r'mul\(\d+,\d+\)',line)
    matches.extend(line_matches)
print(matches)
sum = 0
for match in matches:
        match = (match[3:])
        #print(match[3:])
        match_tuple = tuple(map(int,match.strip('()').split(',')))
        sum += match_tuple[0]*match_tuple[1]
        print(match_tuple)

print(sum)

# Part 2
matches = []
dos = []
donts = []
instruction_set = []
flag = True
sum = 0
for line in lines:
    #print(line)
    instruction_set_line = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)',line)
    line_matches = re.findall(r'mul\(\d+,\d+\)',line)
    instruction_set.extend(instruction_set_line)
print(instruction_set)
for instruction in instruction_set:
    if instruction=="do()":
        flag = True
    elif instruction=="don't()":
        flag = False
    elif flag:
        match = (instruction[3:])
        match_tuple = tuple(map(int,match.strip('()').split(',')))
        sum += match_tuple[0]*match_tuple[1]
print(sum)