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
            if not bank:
                continue
            
            # Efficient way to find max(10*d1 + d2) with index(d1) < index(d2)
            # Precompute max digit to the right of each index
            n = len(bank)
            if n < 2:
                continue
                
            digits = [int(d) for d in bank]
            
            # max_to_right[i] will store the maximum value from digits[i+1:]
            max_to_right = [0] * n
            current_max = -1
            for i in range(n - 1, 0, -1):
                if digits[i] > current_max:
                    current_max = digits[i]
                max_to_right[i-1] = current_max
            
            max_bank_joltage = 0
            for i in range(n - 1):
                joltage = 10 * digits[i] + max_to_right[i]
                if joltage > max_bank_joltage:
                    max_bank_joltage = joltage
            
            total_joltage += max_bank_joltage
            
    print(f"Total Output Joltage: {total_joltage}")

solve()