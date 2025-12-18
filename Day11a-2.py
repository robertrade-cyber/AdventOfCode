def solve_reactor_part2(file_path):
    adj = {}
    with open(file_path, 'r') as f:
        for line in f:
            if ':' not in line: continue
            name, targets = line.split(':')
            adj[name.strip()] = targets.strip().split()

    memo = {}

    def count_paths(start_node, end_node):
        """Standard memoized path counting between any two nodes."""
        if start_node == end_node:
            return 1
        
        state = (start_node, end_node)
        if state in memo:
            return memo[state]
        
        if start_node not in adj:
            return 0
        
        total = 0
        for neighbor in adj[start_node]:
            total += count_paths(neighbor, end_node)
        
        memo[state] = total
        return total

    # Case 1: Path visits dac then fft
    # svr -> dac -> fft -> out
    order_1 = (count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out'))
    
    # Case 2: Path visits fft then dac
    # svr -> fft -> dac -> out
    order_2 = (count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out'))

    return order_1 + order_2

result = solve_reactor_part2('Day11.txt')
print(f"Number of paths visiting both dac and fft: {result}")