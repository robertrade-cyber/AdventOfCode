# Day 2 Part 2 - Advent of Code 2025
# Reads ranges from Day2.txt

with open('Day2.txt', 'r') as f:
    input_line = f.read().strip()

# Parse ranges
ranges = []
for part in input_line.split(','):
    if part:
        start_str, end_str = part.split('-')
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

# Function to check if a number consists of a sequence repeated at least twice
def is_invalid(n):
    s = str(n)
    n_len = len(s)
    # Try all possible repeat lengths (periods) that divide the total length
    # The period must divide n_len, and the repeat count >= 2
    for period in range(1, n_len // 2 + 1):  # period from 1 to half length
        if n_len % period == 0:
            repeat_unit = s[:period]
            repeat_count = n_len // period
            if repeat_count >= 2 and s == repeat_unit * repeat_count:
                return True
    return False

# Sum all invalid IDs
total_sum = 0
for start, end in ranges:
    for num in range(start, end + 1):
        if is_invalid(num):
            total_sum += num

print("Part 2 Sum of invalid IDs:", total_sum)