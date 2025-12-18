def solve_day4(filename):
    try:
        with open(filename, 'r') as f:
            grid = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return "Error: Day4.txt not found."

    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0

    # Define the 8 directions for neighbors (dr, dc)
    neighbors_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            # Only check if the current cell is a roll of paper
            if grid[r][c] == '@':
                adjacent_rolls = 0
                
                # Check all 8 neighbors
                for dr, dc in neighbors_offsets:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary check
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent_rolls += 1
                
                # Condition: Fewer than 4 rolls in the adjacent positions
                if adjacent_rolls < 4:
                    accessible_count += 1
                    
    return accessible_count

# Run the script
if __name__ == "__main__":
    result = solve_day4('Day4.txt')
    print(f"Total Accessible Rolls: {result}")