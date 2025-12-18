import functools
import operator

def solve_day6(filename):
    try:
        with open(filename, 'r') as f:
            # Load all lines and remove trailing newline characters
            lines = [line.rstrip('\n\r') for line in f]
    except FileNotFoundError:
        return "Error: Day6.txt not found."

    if not lines:
        return 0
        
    # Step 1: Standardize length by padding with spaces (create a 2D grid)
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    
    num_rows = len(grid)
    num_cols = max_len
    
    # Step 2: Identify "blank" columns (columns that are entirely whitespace)
    is_blank = []
    for j in range(num_cols):
        column_chars = "".join(grid[i][j] for i in range(num_rows))
        is_blank.append(column_chars.strip() == "")
        
    # Step 3: Group contiguous non-blank columns into segments
    segments = []
    start = None
    for j in range(num_cols):
        if not is_blank[j]:
            if start is None:
                start = j
        else:
            if start is not None:
                segments.append((start, j - 1))
                start = None
    if start is not None:
        segments.append((start, num_cols - 1))
        
    # Step 4: Process each segment (each problem)
    grand_total = 0
    for s_start, s_end in segments:
        numbers = []
        # The operation symbol is in the very last row
        op_symbol = grid[-1][s_start:s_end+1].strip()
        
        # All rows above the last contain the numbers
        for r in range(num_rows - 1):
            num_str = grid[r][s_start:s_end+1].strip()
            if num_str:
                numbers.append(int(num_str))
        
        # Step 5: Perform the math and update the grand total
        if op_symbol and numbers:
            if op_symbol == '+':
                grand_total += sum(numbers)
            elif op_symbol == '*':
                # Multiply all numbers together
                result = functools.reduce(operator.mul, numbers, 1)
                grand_total += result
            
    return grand_total

# Run the script
if __name__ == "__main__":
    result = solve_day6('Day6.txt')
    print(f"The grand total is: {result}")