import time
import csv
import numpy as np
import pandas as pd
start_time = time.time()

lines = []
with open('input.txt') as file:
    for line in file:
        values = line.split()
        lines.append(values)
count = 0
count2 = 0
df = pd.DataFrame(lines)
print(df.head())
df.to_csv("output.csv", index=False, header=False)
print(count)
print(count2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
with open('sol.txt', "a") as f:
    f.write(f"{int(time.time())}: P1: {count} P2: {count2}\n")