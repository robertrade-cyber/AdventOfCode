# Day 7 Part 2 - Quantum Tachyon Manifold (Many-Worlds Timelines)
# Counts the number of timelines (ways to exit)

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

# Ways to reach each cell: 2D list
ways = [[0 for _ in range(cols)] for _ in range(rows + 1)]  # extra row for bottom exits

# Start with 1 timeline below S
ways[start_row + 1][start_col] = 1

total_timelines = 0

for r in range(start_row + 1, rows):
    for c in range(cols):
        if ways[r][c] > 0:
            this_ways = ways[r][c]
            if grid[r][c] == '^':
                # Split: add to left and right in next row
                left_c = c - 1
                right_c = c + 1
                # Left
                if 0 <= left_c < cols:
                    ways[r + 1][left_c] += this_ways
                else:
                    total_timelines += this_ways  # exit side
                # Right
                if 0 <= right_c < cols:
                    ways[r + 1][right_c] += this_ways
                else:
                    total_timelines += this_ways  # exit side
            else:
                # Continue down
                ways[r + 1][c] += this_ways

# All ways that reach the bottom row (r == rows) are exits
for c in range(cols):
    total_timelines += ways[rows][c]

print("Number of different timelines:", total_timelines)