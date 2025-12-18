# Day 3 Part 2 - Advent of Code 2025
# Reads banks from Day3.txt and computes the largest 12-digit joltage per bank

def get_max_12_digit(bank, k=12):
    if len(bank) < k:
        return 0  # Impossible, but safe
    stack = []
    n = len(bank)
    to_remove = n - k  # Number of digits we can skip
    for i in range(n):
        digit = int(bank[i])
        # Remove smaller digits from stack while we can skip more
        while stack and to_remove > 0 and digit > stack[-1]:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    # If still need to remove (sequence was non-decreasing)
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    # Take first k digits (the largest possible in order)
    num_str = ''.join(map(str, stack[:k]))
    return int(num_str)

# Read the file
with open('Day3.txt', 'r') as f:
    banks = [line.strip() for line in f if line.strip()]

# Calculate total
total_joltage = 0
for bank in banks:
    max_joltage = get_max_12_digit(bank)
    total_joltage += max_joltage

print("Part 2 Total output joltage:", total_joltage)