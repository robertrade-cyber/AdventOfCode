def find_largest_red_tile_rectangle(file_path):
    points = []
    # 1. Parse the input file to get all red tile coordinates
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                points.append((x, y))
    
    max_area = 0
    num_points = len(points)
    
    # 2. Compare every pair of points to find the maximum area
    # Note: Area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    for i in range(num_points):
        x1, y1 = points[i]
        for j in range(i + 1, num_points):
            x2, y2 = points[j]
            
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            
            if area > max_area:
                max_area = area
                
    return max_area

# Run the solver on your specific puzzle input
largest_area = find_largest_red_tile_rectangle('Day9.txt')
print(f"The largest area of any rectangle is: {largest_area}")