import time
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
empty_index = lines.index('')
ranges = lines[:empty_index]
ids = lines[empty_index+1:]
fresh_ingredients = []
count = 0
count2 = 0
for i in ranges:
    r = i.split('-')
    fresh_ingredients.append((int(r[0]),int(r[1])))

fresh_ingredients.sort(key=lambda x: x[0])
merged = []
for current_start, current_end in fresh_ingredients:
    if not merged or current_start > merged[-1][1]:
        merged.append([current_start, current_end])
    else:
        merged[-1][1] = max(merged[-1][1], current_end)
print(merged)
for interval in merged:
    count2 += interval[1] - interval[0] + 1

for k in ids:
    for a,b in fresh_ingredients:
        if a<=int(k)<=b:
            count += 1
            break

print(count)
print(count2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
with open('sol.txt', "a") as f:
    f.write(f"{int(time.time())}: P1: {count} P2: {count2}\n")