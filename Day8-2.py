import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

# Read points with index
with open('Day8.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

points = []
for line in lines:
    x, y, z = map(int, line.split(','))
    points.append((x, y, z))

n = len(points)

# All edges: (dist, i, j, x_i, x_j)
edges = []
for i in range(n):
    for j in range(i + 1, n):
        xi, yi, zi = points[i]
        xj, yj, zj = points[j]
        dist = math.sqrt((xi - xj)**2 + (yi - yj)**2 + (zi - zj)**2)
        edges.append((dist, i, j, points[i][0], points[j][0]))

# Sort by distance
edges.sort()

dsu = DSU(n)
components = n
last_x_product = None

for dist, i, j, xi, xj in edges:
    if dsu.union(i, j):
        components -= 1
        if components == 1:
            last_x_product = xi * xj
            break

print("Last connecting X product:", last_x_product)