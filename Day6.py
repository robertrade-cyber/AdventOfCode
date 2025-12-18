# Day 6 Part 1 - Advent of Code 2025 (Corrected)
# Groups problems by non-blank column blocks

from functools import reduce
import operator

# Read and prepare the grid
with open('Day6.txt', 'r') as f:
    lines = [line.rstrip('\n\r') for line in f]

if not lines:
    print("Empty file")
    exit()

# Pad all lines to the same length with spaces on the right
max_len = max(len(line) for line in lines)
grid = [line.ljust(max_len) for line in lines]

rows = len(grid)
cols = max_len

# Identify blank columns (all spaces across all rows)
blank_cols = []
for j in range(cols):
    col_content = ''.join(grid[i][j] for i in range(rows))
    blank_cols.append(col_content.strip() == '')

# Find contiguous segments of non-blank columns → each is one problem
segments = []
start = None
for j in range(cols):
    if not blank_cols[j]:
        if start is None:
            start = j
    else:
        if start is not None:
            segments.append((start, j - 1))  # inclusive end
            start = None
if start is not None:
    segments.append((start, cols - 1))

# Process each problem segment
grand_total = 0
for seg_start, seg_end in segments:
    # Extract operation from the bottom row within this segment
    op_str = grid[-1][seg_start:seg_end + 1].strip()
    if not op_str or op_str not in {'+', '*'}:
        continue  # skip invalid (shouldn't happen)

    op = op_str

    # Extract numbers from all rows above the bottom
    numbers = []
    for r in range(rows - 1):
        num_str = grid[r][seg_start:seg_end + 1].strip()
        if num_str:  # ignore empty lines in the block
            numbers.append(int(num_str))

    # Compute result
    if op == '+':
        result = sum(numbers)
    else:  # '*'
        result = reduce(operator.mul, numbers, 1)

    grand_total += result

print("Grand total:", grand_total)