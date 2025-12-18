def solve_day5(filename):
    ranges = []
    available_ids = []
    
    try:
        with open(filename, 'r') as f:
            content = f.read().strip().split('\n\n')
            
            # 1. Parse Ranges
            range_lines = content[0].split('\n')
            for line in range_lines:
                if '-' in line:
                    start, end = map(int, line.split('-'))
                    ranges.append((start, end))
            
            # 2. Parse Available IDs
            id_lines = content[1].split('\n')
            available_ids = [int(line.strip()) for line in id_lines if line.strip()]
            
    except FileNotFoundError:
        return "Error: Day5.txt not found."
    except IndexError:
        return "Error: File format incorrect. Ensure there is a blank line between ranges and IDs."

    # 3. Merge Overlapping Ranges (Optimization)
    if not ranges:
        return 0
        
    ranges.sort()
    merged_ranges = []
    curr_start, curr_end = ranges[0]
    
    for next_start, next_end in ranges[1:]:
        # If the next range overlaps or is adjacent to the current one
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    merged_ranges.append((curr_start, curr_end))

    # 4. Count Fresh IDs
    fresh_count = 0
    for val in available_ids:
        # Check if the ID falls into any of the fresh ranges
        for start, end in merged_ranges:
            if start <= val <= end:
                fresh_count += 1
                break # Move to the next ID once a match is found
                
    return fresh_count

# Run the script
if __name__ == "__main__":
    result = solve_day5('Day5.txt')
    print(f"Total Fresh Ingredient IDs: {result}")