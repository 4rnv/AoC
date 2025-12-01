import time
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")