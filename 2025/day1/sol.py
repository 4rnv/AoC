import time
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
#print(lines)
pointer = 50
count = 0
count2 = 0

for line in lines:
    if line[0]=='R':
        value = int(line[1:])
    else:
        value = int(line[1:])*-1
    pointer = (pointer+value)%100
    if(pointer==0):
        count += 1
print(count)

pointer = 50
count2 = 0
for line in lines:
    if line[0]=='R':
        sign, value = 1, int(line[1:])
    else:
        sign, value = -1, int(line[1:])
    for i in range(value):
        pointer = (pointer+sign) % 100
        if(pointer==0):
            count2 += 1
print(count2)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")