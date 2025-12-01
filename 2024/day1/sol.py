# I used Excel for Day 1 so this file doesn't actually do anything.
with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)