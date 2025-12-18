lines = open('Day12.txt', 'r').read().splitlines()

# Parse shapes (first 6)
shapes = []
i = 0
while i < len(lines):
    line = lines[i].strip()
    if line and ':' in line:
        shape = []
        i += 1
        while i < len(lines) and lines[i].strip() and ':' not in lines[i]:
            shape.append(lines[i].rstrip())
            i += 1
        if shape:
            shapes.append(shape)
    else:
        i += 1

# Parse regions
regions = []
for line in lines:
    line = line.strip()
    if line and 'x' in line and ':' in line:
        parts = line.split(':')
        size_str = parts[0].strip()
        w, h = map(int, size_str.split('x'))
        counts_str = parts[1].strip()
        counts = list(map(int, counts_str.split()))
        regions.append((w, h, counts))

# Precompute # count for each shape
hash_counts = []
for shape in shapes:
    count = sum(row.count('#') for row in shape)
    hash_counts.append(count)

# Count fitting regions
fit_count = 0
for w, h, counts in regions:
    area = w * h
    needed = 0
    for idx, cnt in enumerate(counts):
        if idx < len(hash_counts):
            needed += cnt * hash_counts[idx]
    if needed <= area:
        fit_count += 1

print("Number of regions that can fit:", fit_count)