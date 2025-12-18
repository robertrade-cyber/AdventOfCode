import functools
import operator

def solve_day6_part2():
    with open('Day6.txt', 'r') as f:
        lines = [line.rstrip('\n\r') for line in f]
    
    if not lines:
        return 0
        
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    
    num_rows = len(grid)
    num_cols = max_len
    
    # Identify blank columns
    is_blank = []
    for j in range(num_cols):
        column_chars = "".join(grid[i][j] for i in range(num_rows))
        is_blank.append(column_chars.strip() == "")
        
    # Find segments
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
        
    grand_total = 0
    # Process problems (order doesn't strictly matter for the final sum, but we'll do right to left)
    for s_start, s_end in reversed(segments):
        # Operator is in the last row
        op_str = grid[-1][s_start:s_end+1].strip()
        if not op_str:
            continue
            
        # Extract numbers from columns, right-to-left
        numbers = []
        for j in range(s_end, s_start - 1, -1):
            # Take digits from top down (rows 0 to num_rows-2)
            num_chars = "".join(grid[i][j] for i in range(num_rows - 1))
            num_str = num_chars.strip()
            if num_str:
                numbers.append(int(num_str))
        
        if not numbers:
            continue
            
        if op_str == '+':
            prob_result = sum(numbers)
        elif op_str == '*':
            prob_result = functools.reduce(operator.mul, numbers, 1)
        else:
            # Should not happen based on puzzle description
            prob_result = 0
            
        grand_total += prob_result
        
    return grand_total

result = solve_day6_part2()
print(f"Grand Total (Part 2): {result}")