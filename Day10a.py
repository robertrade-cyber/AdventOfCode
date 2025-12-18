import re
import itertools

def solve_factory():
    def parse_line(line):
        target_str = re.search(r'\[(.*?)\]', line).group(1)
        target = [1 if c == '#' else 0 for c in target_str]
        buttons_raw = re.findall(r'\((.*?)\)', line)
        buttons = []
        for b in buttons_raw:
            vec = [0] * len(target)
            for idx in map(int, b.split(',')):
                vec[idx] = 1
            buttons.append(vec)
        return target, buttons

    def get_min_presses(target, buttons):
        num_lights = len(target)
        num_buttons = len(buttons)
        # Augmented matrix [Buttons^T | Target]
        matrix = []
        for l_idx in range(num_lights):
            row = [buttons[b_idx][l_idx] for b_idx in range(num_buttons)]
            row.append(target[l_idx])
            matrix.append(row)
            
        # Gaussian Elimination
        pivot_row = 0
        pivots = []
        for j in range(num_buttons):
            if pivot_row >= num_lights: break
            for i in range(pivot_row, num_lights):
                if matrix[i][j]:
                    matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
                    break
            else: continue
            pivots.append((pivot_row, j))
            for i in range(num_lights):
                if i != pivot_row and matrix[i][j]:
                    for k in range(j, num_buttons + 1):
                        matrix[i][k] ^= matrix[pivot_row][k]
            pivot_row += 1

        # Base solution
        particular = [0] * num_buttons
        for r, c in pivots:
            particular[c] = matrix[r][num_buttons]
            
        # Null space basis (Free variables)
        pivot_cols = {c for r, c in pivots}
        basis = []
        for j in range(num_buttons):
            if j not in pivot_cols:
                vec = [0] * num_buttons
                vec[j] = 1
                for r, c in pivots:
                    vec[c] = matrix[r][j]
                basis.append(vec)
        
        # Search for minimum weight solution
        min_w = num_buttons + 1
        for combo in itertools.product([0, 1], repeat=len(basis)):
            sol = list(particular)
            for i, bit in enumerate(combo):
                if bit:
                    sol = [sol[k] ^ basis[i][k] for k in range(num_buttons)]
            min_w = min(min_w, sum(sol))
        return min_w

    total = 0
    with open('Day10.txt', 'r') as f:
        for line in f:
            if line.strip():
                t, b = parse_line(line)
                total += get_min_presses(t, b)
    return total

print(f"Fewest total presses: {solve_factory()}")