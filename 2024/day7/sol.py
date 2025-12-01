from itertools import product

def mul(numbers):
    result = 1
    for number in numbers:
        result = result * number
    return result

def add(numbers):
    return sum(numbers)

def recursion(index, numbers, total, target):
    if index==(len(numbers)):
        return total==target
    return (recursion(index+1,numbers,total+numbers[index],target) or recursion(index+1,numbers,total*numbers[index],target))

def check(target, numbers):
    if(mul(numbers)==target):
        return True,target
    if(add(numbers)==target):
        return True,target
    if(recursion(0, numbers, 0, target)):
        return True,target
    else:
        return False, None

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i]=='||':
            result = int(str(result)+str(numbers[i+1]))
    return result

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)
lines_list = []
for line in lines:
    line_list = line.split(": ")
    lines_list.append(line_list)
print(lines_list)
count = 0
sum_targets = 0
targets = [int(line_list[0]) for line_list in lines_list]
print(targets)
supernumbers = [line_list[1].split(" ") for line_list in lines_list]
supernumbers = [[int(number) for number in numberline] for numberline in supernumbers]
print(supernumbers)
for target,numbers in zip(targets,supernumbers):
    if(len(numbers)==1):
        if numbers[0]==target:
            sum_targets+=target
            count += 1
        continue
    operator_positions = len(numbers) - 1
    for operators in product(['+', '*', '||'], repeat=operator_positions):
        if evaluate_expression(numbers, operators) == target:
            sum_targets += target
            count += 1
            break
    # x, valid_target = check(target,numbers)
    # if x:
    #     sum_targets += valid_target
    #     count += 1
print(count)
print(sum_targets)