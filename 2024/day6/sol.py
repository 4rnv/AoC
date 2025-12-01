import time
start_time = time.time()

def rotate(current_direction):
    return (current_direction + 1) % 4

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
# print(lines)
grid = dict()
directions = [(-1,0),(0,1),(1,0),(0,-1)] # up, right, down, left
visited = set()

for i,row in enumerate(lines):
    for j,char in enumerate(row):
        grid[(i,j)] = char
position = [65, 85]
# print(grid)
current_direction = 0

while tuple(position) in grid:
    visited.add(tuple(position))
    move = (position[0]+directions[current_direction][0],position[1]+directions[current_direction][1])
    if move in grid and grid[move]=="#":
        current_direction = rotate(current_direction)
    position[0] += directions[current_direction][0]
    position[1] += directions[current_direction][1]
print(len(visited))

# Part 2
def explore(obst):
    visited = set()
    current_direction = 0
    loop = False
    position= [65,85]
    while tuple(position) in grid:
        visited.add((tuple(position), current_direction))
        forward = (position[0]+directions[current_direction][0], position[1]+directions[current_direction][1])
        while forward == obst or (forward in grid and grid[forward] == "#"):
            current_direction = rotate(current_direction)
            forward = (position[0]+directions[current_direction][0], position[1]+directions[current_direction][1])
        position[0] += directions[current_direction][0]
        position[1] += directions[current_direction][1]
        if (tuple(position), current_direction) in visited:
            loop = True
            break
    return visited, loop

total = 0
options, loop = explore(obst=None)
options = set(i[0] for i in options)
options.remove(tuple([65,85]))
for option in options:
    path, loop = explore(option)
    if loop:
        total += 1
print(total)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")