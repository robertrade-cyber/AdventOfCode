def solve_day7():
    with open('Day7.txt', 'r') as f:
        grid = [line.rstrip('\r\n') for line in f]
    
    if not grid:
        return 0
        
    # Find S
    s_row, s_col = -1, -1
    for r, row in enumerate(grid):
        if 'S' in row:
            s_row = r
            s_col = row.index('S')
            break
            
    if s_row == -1:
        return "S not found"
        
    width = max(len(row) for row in grid)
    # Ensure all rows have same length for safe indexing
    grid = [row.ljust(width) for row in grid]
    
    beams = {s_col}
    total_splits = 0
    
    # Process from the row S is in, but the beam moves DOWN.
    # So we process rows from s_row + 1 onwards.
    # Note: If a splitter was on the same row as S, the beam hasn't hit it yet.
    # "The incoming tachyon beam extends downward from S until it reaches the first splitter"
    for r in range(s_row + 1, len(grid)):
        next_beams = set()
        for c in beams:
            # Check if beam hits a splitter in this row
            if 0 <= c < len(grid[r]) and grid[r][c] == '^':
                total_splits += 1
                # Split creates two new beams at c-1 and c+1
                next_beams.add(c - 1)
                next_beams.add(c + 1)
            else:
                # Beam continues downward in same column
                next_beams.add(c)
        
        # Update active beams, filtering out-of-bounds
        beams = {b for b in next_beams if 0 <= b < width}
        if not beams:
            break
            
    return total_splits

print(solve_day7())