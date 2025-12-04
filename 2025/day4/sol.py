import time
start_time = time.time()

def check_adjacent(grid, i, j):
    def in_bound(ni, nj):
        return 0 <= ni < len(grid) and 0 <= nj < len(grid[0])

    ats = 0
    if in_bound(i+1, j+1) and grid[i+1][j+1]=='@':
        ats += 1
    if in_bound(i+1, j) and grid[i+1][j]=='@':
        ats += 1
    if in_bound(i+1, j-1) and grid[i+1][j-1]=='@':
        ats += 1
    if in_bound(i, j+1) and grid[i][j+1]=='@':
        ats += 1
    if in_bound(i, j-1) and grid[i][j-1]=='@':
        ats += 1
    if in_bound(i-1, j+1) and grid[i-1][j+1]=='@':
        ats += 1
    if in_bound(i-1, j) and grid[i-1][j]=='@':
        ats += 1
    if in_bound(i-1, j-1) and grid[i-1][j-1]=='@':
        ats += 1
    return ats < 4

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
#print(lines)
grid = []

for line in lines:
    gridline = list(line)
    grid.append(gridline)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='@':
            if check_adjacent(grid, i, j):
                count +=1
print("Part 1: ", count)

count2 = 0
newcount = 1
while newcount > 0:
    to_flip = []
    newcount = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='@':
                if check_adjacent(grid, i, j):
                    newcount +=1
                    to_flip.append((i,j))
    for (r, c) in to_flip:
        grid[r][c] = 'x'
    # print("Newcount: ", newcount)
    count2 += newcount
print("Part 2: ", count2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")