def is_sorted(line_list: list):
    if all(line_list[i] <= line_list[i + 1] for i in range(len(line_list) - 1)) and all(1 <= abs(line_list[i] - line_list[i + 1]) <=3 for i in range(len(line_list) - 1)):
        return True
    elif all(line_list[i] >= line_list[i + 1] for i in range(len(line_list) - 1)) and all(1 <= abs(line_list[i] - line_list[i + 1]) <=3 for i in range(len(line_list) - 1)):
        return True
    return False

def is_sorted_damp(line_list : list):
    if is_sorted(line_list):
        return True
    else:
        for num in range(len(line_list)):
            new_list = line_list[:num] + line_list[num + 1:]
            y = is_sorted(new_list)
            if(y==True):
                return True
    return False

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)
lines_list = []
count = 0
for line in lines:
    line_list = line.split()
    line_list = [int(x) for x in line_list]
    lines_list.append(line_list)
print(lines_list)

# Part 1
for line_list in lines_list:
    x = is_sorted(line_list)
    if(x==True):
        count += 1
print(count)

# Part 2
count_damp = 0
for line_list in lines_list:
    x = is_sorted_damp(line_list)
    if(x==True):
        count_damp += 1
print(count_damp)