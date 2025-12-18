import sys
sys.setrecursionlimit(5000)  # Adjust if needed for deeper graphs

def count_paths_visiting_both(file_path='Day11.txt'):
    # Build adjacency list
    adj = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if ':' not in line:
                continue
            name, targets_str = line.split(':', 1)
            name = name.strip()
            targets = targets_str.strip().split()
            adj[name] = targets

    # Memoization: (current_node, visited_dac, visited_fft)
    memo = {}

    def get_paths(current, visited_dac, visited_fft):
        if current == 'out':
            return 1 if visited_dac and visited_fft else 0
        
        key = (current, visited_dac, visited_fft)
        if key in memo:
            return memo[key]
        
        if current not in adj:
            total = 0
        else:
            total = 0
            new_dac = visited_dac or (current == 'dac')
            new_fft = visited_fft or (current == 'fft')
            for next_device in adj[current]:
                total += get_paths(next_device, new_dac, new_fft)
        
        memo[key] = total
        return total

    return get_paths('svr', False, False)

total = count_paths_visiting_both()
print(f"Paths visiting both dac and fft: {total}")