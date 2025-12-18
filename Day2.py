# Day 2 - Advent of Code 2025
# Reads from Day2.txt (one long line with comma-separated ranges)

# Read the input from the file
with open('Day2.txt', 'r') as f:
    input_line = f.read().strip()  # Reads the entire file and removes whitespace/newlines

# Parse the ranges
ranges = []
for part in input_line.split(','):
    if part:  # Skip any empty parts
        start_str, end_str = part.split('-')
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

# Function to check if a number is invalid (its digits are some sequence repeated exactly twice)
def is_invalid(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:          # Odd length can't be two equal halves
        return False
    half = length // 2
    return s[:half] == s[half:]

# Sum all invalid IDs across all ranges
total_sum = 0
invalid_ids = []  # Optional: keep track of which ones for debugging

for start, end in ranges:
    for num in range(start, end + 1):
        if is_invalid(num):
            total_sum += num
            invalid_ids.append(num)  # Remove this line if you don't want the list

print("Sum of invalid IDs:", total_sum)

# Optional: print the actual invalid IDs found
# print("Invalid IDs found:", invalid_ids)