import sys
sys.setrecursionlimit(2000)  # Safe for deeper graphs

def count_reactor_paths(file_path='Day11.txt'):
    # Build adjacency list: device -> list of output devices
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

    # Memoization cache
    memo = {}

    def get_paths(current):
        if current == 'out':
            return 1
        if current in memo:
            return memo[current]
        if current not in adj:
            return 0

        total = 0
        for next_device in adj[current]:
            total += get_paths(next_device)

        memo[current] = total
        return total

    return get_paths('you')

total = count_reactor_paths()
print(f"Total different paths from you to out: {total}")