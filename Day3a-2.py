def solve_day3_part2(filename):
    total_joltage = 0
    target_length = 12
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                bank = line.strip()
                if not bank:
                    continue
                
                # Number of digits we MUST remove
                to_remove = len(bank) - target_length
                
                if to_remove < 0:
                    # If bank is shorter than 12, the rules might imply 
                    # taking all of them, but based on the puzzle, 
                    # banks are likely >= 12.
                    total_joltage += int(bank)
                    continue

                stack = []
                removed = 0
                
                for digit in bank:
                    # While we have removals left and the current digit is 
                    # bigger than the last one we kept, discard the smaller digit.
                    while removed < to_remove and stack and stack[-1] < digit:
                        stack.pop()
                        removed += 1
                    stack.append(digit)
                
                # If we haven't removed enough (e.g., the string was 9876...),
                # remove the remaining from the end.
                result_digits = stack[:target_length]
                
                # Join and add to total
                total_joltage += int("".join(result_digits))
                
        return total_joltage

    except FileNotFoundError:
        return "Error: Day3.txt not found."

# Run and print the result
print(f"New Total Output Joltage: {solve_day3_part2('Day3.txt')}")