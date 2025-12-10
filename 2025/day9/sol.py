import time
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
points = []
for line in lines:
    x,y = line.split(',')
    points.append((int(x),int(y)))
max_area = 0
point1 = None
point2 = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        height = abs(y2 - y1) + 1
        width = abs(x2 - x1) + 1
        area = height*width
        if area > max_area:
            max_area = area
            point1, point2 = points[i], points[j]
print(f"Points: {point1} and {point2}")
print("Area of max rectangle: ", max_area)

def point_in_polygon(x, y, polygon):
    inside = False
    n = len(polygon)
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p2y != p1y:
                        x_intersection = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= x_intersection:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside

red_green_tiles = set(points)
max_area2 = 0
point1 = None
point2 = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        valid = True
        for x in range(min_x, max_x + 1):
            if not valid:
                break
            for y in range(min_y, max_y + 1):
                if (x, y) not in red_green_tiles and not point_in_polygon(x, y, points):
                    print(x,y)
                    valid = False
                    break
        if valid:
            height = abs(y2 - y1) + 1
            width = abs(x2 - x1) + 1
            area = height*width
            if area > max_area2:
                max_area2 = area
                point1, point2 = points[i], points[j]

print(f"Points2: {point1} and {point2}")
print("Area of max rectangle2: ", max_area2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
with open('sol.txt', "a") as f:
    f.write(f"{int(time.time())}: P1: {max_area} P2: {max_area2}\n")