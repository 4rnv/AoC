import time
start_time = time.time()

def check(grid,i,j):
    count = 0
    if grid[i+1][j+1]=="M" and grid[i+1][j-1]=="M" and grid[i-1][j-1]=="S" and grid[i-1][j+1]=="S":
        count += 1
    elif grid[i+1][j+1]=="M" and grid[i+1][j-1]=="S" and grid[i-1][j-1]=="S" and grid[i-1][j+1]=="M":
        count += 1
    elif grid[i+1][j+1]=="S" and grid[i+1][j-1]=="M" and grid[i-1][j-1]=="M" and grid[i-1][j+1]=="S":
        count += 1
    elif grid[i+1][j+1]=="S" and grid[i+1][j-1]=="S" and grid[i-1][j-1]=="M" and grid[i-1][j+1]=="M":
        count += 1
    return count

with open('input.txt') as file:
#with open('bigboy.txt') as file:

    lines = [line.rstrip() for line in file.readlines()]
#print(lines)
grid = []
for line in lines:
    row = list(line)
    grid.append(row)

x_word = "MAS"
answer=0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=="A" and (0 < i < len(grid) -1) and (0 < j < len(grid[i]) -1):
            if check(grid,i,j):
                answer+=1

print(answer)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")