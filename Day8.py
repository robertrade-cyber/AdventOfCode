import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return  # redundant, no change
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

# Read points
with open('Day8.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

points = [tuple(map(int, line.split(','))) for line in lines]
n = len(points)

# All edges
edges = []
for i in range(n):
    for j in range(i + 1, n):
        dist = math.sqrt(sum((a - b)**2 for a, b in zip(points[i], points[j])))
        edges.append((dist, i, j))

edges.sort()

# Add the first 1000 shortest edges (redundant OK)
dsu = DSU(n)
for k in range(min(1000, len(edges))):
    dist, u, v = edges[k]
    dsu.union(u, v)

# Component sizes
sizes = [dsu.size[i] for i in range(n) if dsu.find(i) == i]
sizes.sort(reverse=True)

top3 = sizes[:3]
print("Three largest:", top3)
print("Product:", top3[0] * top3[1] * top3[2])