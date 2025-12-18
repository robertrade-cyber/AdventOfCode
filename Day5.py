# Day 5 Part 1 - Advent of Code 2025
# Reads fresh ranges and available IDs from Day5.txt, counts fresh IDs

# Read the file
with open('Day5.txt', 'r') as f:
    lines = f.readlines()

# Parse fresh ranges (first section before blank line)
fresh_ranges = []
i = 0
while i < len(lines) and lines[i].strip():
    start_end = lines[i].strip().split('-')
    start = int(start_end[0])
    end = int(start_end[1])
    fresh_ranges.append((start, end))
    i += 1

# Skip blank lines
while i < len(lines) and not lines[i].strip():
    i += 1

# Parse available IDs (second section)
available_ids = []
while i < len(lines):
    id_str = lines[i].strip()
    if id_str:
        available_ids.append(int(id_str))
    i += 1

# Function to check if ID is in any fresh range
def is_fresh(id_val, ranges):
    for start, end in ranges:
        if start <= id_val <= end:
            return True
    return False

# Count fresh IDs
fresh_count = 0
for id_val in available_ids:
    if is_fresh(id_val, fresh_ranges):
        fresh_count += 1

print("Number of fresh ingredient IDs:", fresh_count)