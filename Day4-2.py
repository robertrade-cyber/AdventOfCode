# Day 4 Part 2 - Advent of Code 2025
# Simulate repeated removal of accessible rolls (@ with <4 neighbors)

from copy import deepcopy

# Read the grid
with open('Day4.txt', 'r') as f:
    grid = [list(line.rstrip('\n')) for line in f]

rows = len(grid)
if rows == 0:
    print("Empty grid")
    exit()
cols = len(grid[0])

# 8 directions for neighbors
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def count_neighbors(g, i, j):
    count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and g[ni][nj] == '@':
            count += 1
    return count

total_removed = 0

changed = True
while changed:
    changed = False
    to_remove = []
    
    # Find all current accessible rolls
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and count_neighbors(grid, i, j) < 4:
                to_remove.append((i, j))
    
    # If none found, stop
    if not to_remove:
        break
    
    # Remove them all at once
    for i, j in to_remove:
        grid[i][j] = '.'
    
    total_removed += len(to_remove)
    changed = True

print("Total rolls of paper that can be removed:", total_removed)