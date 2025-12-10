import time
import numpy as np
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
# print(lines)
count = 0
count2 = 0
x = []
y = []
z = []
for i, line in enumerate(lines):
    x_,y_,z_ = line.split(',')
    x.append(int(x_))
    y.append(int(y_))
    z.append(int(z_))
coordinates = np.array(list(zip(x, y, z)))
print(coordinates)
num_coords = coordinates.shape[0]
distance_matrix = np.zeros((num_coords, num_coords))
for i in range(num_coords):
    for j in range(num_coords):
        distance_matrix[i, j] = np.sqrt(np.sum((coordinates[i] - coordinates[j]) ** 2))
print(distance_matrix)
print(count)
print(count2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
with open('sol.txt', "a") as f:
    f.write(f"{int(time.time())}: P1: {count} P2: {count2}\n")