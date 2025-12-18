# Day 9 - Largest Rectangle with Opposite Red Corners

# Read points
with open('Day9.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

points = []
for line in lines:
    x, y = map(int, line.split(','))
    points.append((x, y))

n = len(points)

max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        if x1 != x2 and y1 != y2:
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_area:
                max_area = area

print("Largest rectangle area:", max_area)