def solve_theater_part2(file_path):
    red_tiles = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                x, y = map(int, line.split(','))
                red_tiles.append((x, y))

    def is_rect_valid(x1, x2, y1, y2, polygon):
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        
        # 1. Point-in-Polygon Check (Ray Casting) for the rectangle center
        cx, cy = (xmin + xmax) / 2.0, (ymin + ymax) / 2.0
        inside = False
        for i in range(len(polygon)):
            p1, p2 = polygon[i], polygon[(i + 1) % len(polygon)]
            if (p1[1] > cy) != (p2[1] > cy):
                vt = (cy - p1[1]) / (p2[1] - p1[1])
                if cx < p1[0] + vt * (p2[0] - p1[0]):
                    inside = not inside
        if not inside: return False
        
        # 2. Check for boundary edge intersections with rectangle interior
        for i in range(len(polygon)):
            p1, p2 = polygon[i], polygon[(i + 1) % len(polygon)]
            if p1[0] == p2[0]: # Vertical Edge
                if xmin < p1[0] < xmax:
                    if not (max(p1[1], p2[1]) <= ymin or min(p1[1], p2[1]) >= ymax):
                        return False
            else: # Horizontal Edge
                if ymin < p1[1] < ymax:
                    if not (max(p1[0], p2[0]) <= xmin or min(p1[0], p2[0]) >= xmax):
                        return False
        return True

    max_area = 0
    n = len(red_tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            # Area calculation (inclusive of boundary tiles)
            current_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            
            if current_area > max_area:
                if is_rect_valid(x1, x2, y1, y2, red_tiles):
                    max_area = current_area
                    
    return max_area

answer = solve_theater_part2('Day9.txt')
print(f"Largest valid rectangle area: {answer}")