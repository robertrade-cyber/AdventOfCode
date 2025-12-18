def solve_day5_part2(filename):
    ranges = []
    
    try:
        with open(filename, 'r') as f:
            # We only need the first section (up to the blank line)
            for line in f:
                line = line.strip()
                if not line: # Stop at the blank line
                    break
                if '-' in line:
                    start, end = map(int, line.split('-'))
                    ranges.append((start, end))
    except FileNotFoundError:
        return "Error: Day5.txt not found."

    if not ranges:
        return 0

    # 1. Sort ranges by the starting ID
    ranges.sort()
    
    merged_ranges = []
    if ranges:
        curr_start, curr_end = ranges[0]
        
        # 2. Iteratively merge overlapping or adjacent ranges
        for next_start, next_end in ranges[1:]:
            # If the next range overlaps or touches the current one
            if next_start <= curr_end + 1:
                curr_end = max(curr_end, next_end)
            else:
                # No overlap: save the completed block and start a new one
                merged_ranges.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        
        # Save the final block
        merged_ranges.append((curr_start, curr_end))
    
    # 3. Sum the count of unique IDs in each merged block
    total_fresh_ids = sum((end - start + 1) for start, end in merged_ranges)
    
    return total_fresh_ids

# Run the script
if __name__ == "__main__":
    result = solve_day5_part2('Day5.txt')
    print(f"Total Unique Fresh IDs: {result}")