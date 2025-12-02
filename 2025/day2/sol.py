import time
import re
start_time = time.time()

with open('bigboy.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
ranges = lines[0].split(',')
invalid_IDs = []
for r in ranges:
    start, end = r.split('-')
    start, end = int(start), int(end)
    for i in range(start, end):
        s = str(i)
        mid = len(s)//2
        if mid == 0: 
            continue
        if i == int(s[:mid]) * (10**mid + 1):
            invalid_IDs.append(i)
print("Sum Part 1:", sum(invalid_IDs))

invalid_IDs = []
for r in ranges:
    start, end = r.split('-')
    start, end = int(start), int(end)
    for i in range(start, end):
        s = str(i)
        mid = len(s)//2
        if mid == 0: 
            continue
        if re.match(r'^(\d+)\1+$', s):
            invalid_IDs.append(i)       
print("Sum Part 2:", sum(invalid_IDs))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")