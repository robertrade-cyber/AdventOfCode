# Day 7 Part 1 - Fixed with visited positions to avoid infinite loop

from collections import deque

# Read the grid
with open('Day7.txt', 'r') as f:
    grid = [line.rstrip('\n') for line in f]

rows = len(grid)
if rows == 0:
    print("Empty grid")
    exit()
cols = len(grid[0])

# Find S
start_row, start_col = None, None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start_row, start_col = r, c
            break
    if start_row is not None:
        break

if start_row is None:
    print("No S found")
    exit()

# BFS with visited set: each (row, col) is processed only once
queue = deque()
queue.append((start_row + 1, start_col))  # start below S

visited = set()
split_count = 0

while queue:
    r, c = queue.popleft()

    # Out of bounds = exit
    if not (0 <= r < rows and 0 <= c < cols):
        continue

    # Skip if already processed
    if (r, c) in visited:
        continue
    visited.add((r, c))

    if grid[r][c] == '^':
        split_count += 1
        # Emit two new beams downward from left/right columns
        queue.append((r + 1, c - 1))
        queue.append((r + 1, c + 1))
    else:
        # Continue downward
        queue.append((r + 1, c))

print("Number of times the beam is split:", split_count)