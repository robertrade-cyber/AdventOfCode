def solve_day4_part2(filename):
    try:
        with open(filename, 'r') as f:
            # Convert grid into a list of lists so we can modify it
            grid = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        return "Error: Day4.txt not found."

    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0
    
    neighbors_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    while True:
        to_remove = []
        
        # Step 1: Identify all currently accessible rolls
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    adjacent_rolls = 0
                    for dr, dc in neighbors_offsets:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                adjacent_rolls += 1
                    
                    if adjacent_rolls < 4:
                        to_remove.append((r, c))
        
        # Step 2: If no rolls were found to remove, we are finished
        if not to_remove:
            break
            
        # Step 3: Remove the identified rolls and update count
        for r, c in to_remove:
            # Check again to handle potential double-counting in the same batch
            if grid[r][c] == '@':
                grid[r][c] = '.'
                total_removed += 1
                
    return total_removed

# Run the script
if __name__ == "__main__":
    result = solve_day4_part2('Day4.txt')
    print(f"Total Rolls Removed: {result}")