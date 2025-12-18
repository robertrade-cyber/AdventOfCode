import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(2000)

def count_reactor_paths(file_path):
    # 1. Build the adjacency list
    adj = {}
    with open(file_path, 'r') as f:
        for line in f:
            if ':' not in line: continue
            name, targets = line.split(':')
            adj[name.strip()] = targets.strip().split()

    # 2. Memoization dictionary to store calculated path counts
    memo = {}

    def get_paths_to_out(current_node):
        # Base Case: We reached the reactor output
        if current_node == 'out':
            return 1
        
        # Return cached result if we've been here before
        if current_node in memo:
            return memo[current_node]
        
        # If the node has no outgoing connections and isn't 'out'
        if current_node not in adj:
            return 0
        
        # Recursive step: Sum paths of all neighbors
        total_paths = 0
        for neighbor in adj[current_node]:
            total_paths += get_paths_to_out(neighbor)
            
        # Store in memo before returning
        memo[current_node] = total_paths
        return total_paths

    return get_paths_to_out('you')

# Solve for your input
total = count_reactor_paths('Day11.txt')
print(f"Total different paths from you to out: {total}")