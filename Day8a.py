import math
from collections import Counter

def solve_playground():
    # 1. Parse coordinates
    points = []
    with open('Day8.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            points.append(list(map(int, line.split(','))))
            
    num_points = len(points)
    
    # 2. Calculate all pairwise squared distances
    pairs = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1, p2 = points[i], points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            pairs.append((dist_sq, i, j))
            
    # 3. Sort pairs by distance
    pairs.sort()
    
    # 4. Take the 1000 shortest connections
    connections = pairs[:1000]
    
    # 5. Union-Find to group junction boxes into circuits
    parent = list(range(num_points))
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            
    for _, idx1, idx2 in connections:
        union(idx1, idx2)
        
    # 6. Calculate circuit sizes
    circuit_counts = Counter(find(i) for i in range(num_points))
    sizes = sorted(circuit_counts.values(), reverse=True)
    
    # 7. Multiply the three largest sizes
    top_3 = sizes[:3]
    product = 1
    for s in top_3:
        product *= s
        
    return top_3, product

top_sizes, result = solve_playground()
print(f"Three largest circuit sizes: {top_sizes}")
print(f"Product: {result}")