def solve_final_connection(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            points.append(list(map(int, line.split(','))))
            
    num_points = len(points)
    
    # 1. Calculate all pairwise squared distances
    pairs = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1, p2 = points[i], points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            pairs.append((dist_sq, i, j))
            
    # 2. Sort pairs by distance (shortest first)
    pairs.sort()
    
    # 3. Union-Find to track connectivity
    parent = list(range(num_points))
    num_circuits = num_points
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i]) # Path compression
        return parent[i]
        
    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False
        
    # 4. Connect boxes until only 1 circuit remains
    last_connection = None
    for _, idx1, idx2 in pairs:
        if union(idx1, idx2):
            num_circuits -= 1
            if num_circuits == 1:
                last_connection = (points[idx1], points[idx2])
                break
                
    # 5. Extract X coordinates and multiply
    x1 = last_connection[0][0]
    x2 = last_connection[1][0]
    return x1, x2, x1 * x2

x_coord1, x_coord2, result = solve_final_connection('Day8.txt')
print(f"Junction Box A (X): {x_coord1}")
print(f"Junction Box B (X): {x_coord2}")
print(f"Product: {result}")