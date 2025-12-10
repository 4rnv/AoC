import pandas as pd
import time
from collections import Counter
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
# print(lines)
count = 0
count2 = 0
data_rows = []
for line in lines:
    data_rows.append(list(line))
# df = pd.DataFrame(data_rows)
# print(df.tail())
start = {lines[0].find('S'): 1}
print(start)
for line in lines:
    if "^" in line:
        new_beams = Counter()
        for b,c in start.items():
            if line[b] == "^":
                count += 1
                new_beams[b - 1] += c
                new_beams[b + 1] += c
            else:
                new_beams[b] += c
        start = new_beams
count2 = sum(new_beams.values())
print(count)
print(count2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
with open('sol.txt', "a") as f:
    f.write(f"{int(time.time())}: P1: {count} P2: {count2}\n")