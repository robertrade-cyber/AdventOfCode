import os

def solve():
    file_path = 'Day3.txt'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return
    
    total_joltage = 0
    with open(file_path, 'r') as f:
        for line in f:
            bank = line.strip()
            if not bank or len(bank) < 2:
                continue
            
            digits = [int(d) for d in bank]
            n = len(bank)
            
            # Precompute the maximum digit to the right of each position
            max_to_right = [0] * n
            current_max = -1
            for i in range(n - 1, -1, -1):  # Go from right to left, including the last
                if i < n - 1:
                    max_to_right[i] = max(current_max, digits[i + 1])
                else:
                    max_to_right[i] = -1  # No right for last, but we don't use it
                if digits[i] > current_max:
                    current_max = digits[i]
            
            # For each possible left position i (0 to n-2), max joltage = 10*digits[i] + max_to_right[i]
            max_bank = 0
            for i in range(n - 1):
                joltage = 10 * digits[i] + max_to_right[i]
                if joltage > max_bank:
                    max_bank = joltage
            
            total_joltage += max_bank
    
    print(f"Total Output Joltage: {total_joltage}")

solve()