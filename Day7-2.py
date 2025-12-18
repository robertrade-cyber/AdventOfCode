from collections import Counter

def solve_quantum_manifold(file_path):
    with open(file_path, 'r') as f:
        grid = [line.rstrip('\n\r') for line in f]
    
    num_rows = len(grid)
    width = max(len(row) for row in grid)
    grid = [row.ljust(width) for row in grid]
    
    # Locate starting point S
    s_row, s_col = -1, -1
    for r in range(num_rows):
        idx = grid[r].find('S')
        if idx != -1:
            s_row, s_col = r, idx
            break
            
    # Track the number of timelines at each column
    # Start with 1 timeline at the column of S
    counts = Counter({s_col: 1})
    total_exited_sides = 0
    
    # Process the manifold row by row
    for r in range(s_row + 1, num_rows):
        next_counts = Counter()
        for col, amount in counts.items():
            # If the particle is within the manifold bounds
            if 0 <= col < width:
                if grid[r][col] == '^':
                    # Timeline splits: one left, one right
                    next_counts[col - 1] += amount
                    next_counts[col + 1] += amount
                else:
                    # Timeline continues straight down
                    next_counts[col] += amount
            else:
                # Particle has already exited the manifold sides
                total_exited_sides += amount
        counts = next_counts
            
    # Total timelines is the sum of those at the bottom + those that exited sides
    return sum(counts.values()) + total_exited_sides

answer = solve_quantum_manifold('Day7.txt')
print(f"Total Timelines: {answer}")