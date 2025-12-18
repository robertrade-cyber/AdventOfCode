# Day 4 Part 1 - Advent of Code 2025
# Reads the grid from Day4.txt and counts accessible rolls (@ with <4 neighbors)

# Read the grid from the file
with open('Day4.txt', 'r') as f:
    grid = [line.rstrip('\n') for line in f]  # Keep exact lines, remove only newline

# Dimensions
rows = len(grid)
if rows == 0:
    print("Empty grid")
else:
    cols = len(grid[0])  # All lines are the same length

# Directions for 8 neighbors
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

count = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            neighbor_count = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                    neighbor_count += 1
            if neighbor_count < 4:
                count += 1

print("Number of accessible rolls:", count)