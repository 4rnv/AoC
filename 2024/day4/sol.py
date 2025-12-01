def is_valid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

def find_word_in_direction(grid, n, m, word, index,
                        x, y, dirX, dirY):
    if index == len(word):
        return True

    if is_valid(x, y, n, m) and word[index] == grid[x][y]:
        return find_word_in_direction(grid, n, m, word, index + 1, 
                                   x + dirX, y + dirY, dirX, dirY)
    return False

def search_word(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):

            if grid[i][j] == word[0]:  
                for dirX, dirY in directions:
                    if find_word_in_direction(grid, n, m, word, 0, 
                                           i, j, dirX, dirY):
                        ans.append([i, j])
    return ans

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
#print(lines)
grid = []
for line in lines:
    row = list(line)
    grid.append(row)
    #grid.extend(row)
print(grid)
word = "XMAS"
ans1 = search_word(grid, word)
print(len(ans1))