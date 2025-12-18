# Day 5 Part 2 - Advent of Code 2025
# Count the total number of unique ingredient IDs covered by the fresh ranges

# Read the file
with open('Day5.txt', 'r') as f:
    lines = f.readlines()

# Parse only the fresh ranges (first section before blank line)
fresh_ranges = []
i = 0
while i < len(lines) and lines[i].strip():
    start_end = lines[i].strip().split('-')
    start = int(start_end[0])
    end = int(start_end[1])
    fresh_ranges.append((start, end))
    i += 1

# To count unique IDs covered by any range, merge overlapping/intersecting ranges
# Sort ranges by start
fresh_ranges.sort(key=lambda x: x[0])

# Merge overlapping or adjacent ranges
merged = []
for current in fresh_ranges:
    if not merged:
        merged.append(list(current))  # [start, end]
    else:
        last = merged[-1]
        # If current overlaps or touches the last merged range
        if current[0] <= last[1] + 1:  # +1 to merge adjacent like 5-10 and 11-15
            last[1] = max(last[1], current[1])
        else:
            merged.append(list(current))

# Calculate total unique IDs
total_fresh = 0
for start, end in merged:
    total_fresh += end - start + 1  # inclusive count

print("Total fresh ingredient IDs:", total_fresh)