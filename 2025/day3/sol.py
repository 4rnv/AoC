import time
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]

print(lines)
sum = 0
for line in lines:
    maxv = 0
    nums = list(line)
    print(nums)
    for i, vali in enumerate(nums):
        for j, valj in enumerate(nums[:i]):
            if int(valj+vali)>maxv:
                maxv = int(valj+vali)
    print(maxv)
    sum+=maxv
print("Part 1: ", sum)

sum2 = 0
for line in lines:
    nums = [int(n) for n in list(line)]
    print(nums)
    left, right = 0, len(nums) - 11
    for i in range(12):
        idx = nums[left:right].index(max(nums[left:right])) + left
        sum2 += nums[idx] * (10**(11 - i))
        left, right = idx + 1, right + 1

print("Part 2: ", sum2)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")