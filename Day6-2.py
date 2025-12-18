import functools
import operator

# Read the file
with open('Day6.txt', 'r') as f:
    lines = [line.rstrip('\n\r') for line in f]

if not lines:
    print("Empty file")
    exit()

# Pad lines to same length
max_len = max(len(line) for line in lines)
grid = [line.ljust(max_len) for line in lines]

rows = len(grid)
cols = max_len

# Transpose for easy column access
columns = [''.join(grid[r][c] for r in range(rows)) for c in range(cols)]

# Blank columns
blank_cols = [col.strip() == '' for col in columns]

# Find problem segments
segments = []
start = None
for j in range(cols):
    if not blank_cols[j]:
        if start is None:
            start = j
    else:
        if start is not None:
            segments.append((start, j - 1))
            start = None
if start is not None:
    segments.append((start, cols - 1))

grand_total = 0
for seg_start, seg_end in segments:
    # Find operation in bottom row within segment
    op = None
    for j in range(seg_start, seg_end + 1):
        bottom = grid[-1][j]
        if bottom in {'+', '*'}:
            op = bottom
            break
    if op is None:
        continue

    # Extract numbers: one per column in segment
    numbers = []
    for j in range(seg_start, seg_end + 1):
        col_str = columns[j]
        # Digits above the bottom (strip spaces)
        digit_part = col_str[:-1].strip()
        if digit_part:
            numbers.append(int(digit_part))

    # Compute result
    if op == '+':
        result = sum(numbers)
    else:
        result = functools.reduce(operator.mul, numbers, 1)

    grand_total += result

print("Part 2 Grand total:", grand_total)