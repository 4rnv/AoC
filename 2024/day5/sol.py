import time
start_time = time.time()

def check(update, rules_list):
    for i in range(len(update)-1,0,-1):
        for j in range(i):
            if(update[j], update[i]) not in rules_list:
                return False
    return True

def fix_this_update_plz(update):
    for i in range(len(update)-1,0,-1):
        for j in range(i):
            if(update[j], update[i]) not in rules_list:
                update[j], update[i] = update[i], update[j]
    return update

def median(valid_update):
    return valid_update[len(valid_update)//2]

with open('section1.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)
rules_list = [(int(before),int(after)) for (before,after) in [line.split('|') for line in lines]]
print(rules_list)

with open('section2.txt') as file2:
    file2_lines = [line2.rstrip() for line2 in file2.readlines()]
print(file2_lines)

printer_updates = [[int(x) for x in line.split(',')] for line in file2_lines]
print(printer_updates)

valid_updates = []
invalid_updates = []
sum = 0
for update in printer_updates:
    if check(update, rules_list):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)
print("Valid Updates: ",len(valid_updates))
print("Invalid Updates: ",len(invalid_updates))

for valid_update in valid_updates:
    sum += median(valid_update)
print("Sum: ", sum)

# Part 2
fixed_updates = []
sum2 = 0

for invalid_update in invalid_updates:
    fixed_updates.append(fix_this_update_plz(invalid_update))
print(len(fixed_updates))

for fixed_update in fixed_updates:
    sum2 += median(fixed_update)
print("Sum2: ", sum2)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")