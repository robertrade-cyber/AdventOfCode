import re
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

def solve_factory_joltage(file_path):
    total_presses = 0
    
    with open(file_path, 'r') as f:
        for line in f:
            if not line.strip(): continue
            
            # 1. Parse counters (targets) and buttons (coefficients)
            joltage_match = re.search(r'\{(.*?)\}', line)
            targets = [int(x) for x in joltage_match.group(1).split(',')]
            num_counters = len(targets)
            
            button_matches = re.findall(r'\((.*?)\)', line)
            buttons = []
            for b_str in button_matches:
                vec = [0] * num_counters
                indices = [int(x) for x in b_str.split(',') if x.strip()]
                for idx in indices:
                    if idx < num_counters:
                        vec[idx] = 1
                buttons.append(vec)
            
            # A matrix: Rows = counters, Columns = buttons
            A = np.array(buttons).T
            b = np.array(targets)
            num_buttons = len(buttons)
            
            # 2. Set up Integer Linear Programming
            # Objective: minimize sum(x_i)
            c = np.ones(num_buttons)
            # Constraints: All x must be integers >= 0
            integrality = np.ones(num_buttons) 
            bounds = Bounds(0, np.inf)
            # Equation: Ax = b
            constraints = LinearConstraint(A, b, b)
            
            # 3. Solve for the specific machine
            res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)
            
            if res.success:
                total_presses += int(round(res.fun))
                
    return total_presses

# Execute the solver
final_answer = solve_factory_joltage('Day10.txt')
print(f"Total fewest presses for all machines: {final_answer}")