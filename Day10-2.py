import pulp

# Read the input
with open('Day10.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

total_presses = 0

for line in lines:
    # Parse diagram (ignore)
    start = line.find('[')
    end = line.find(']')
    diagram = line[start+1:end] if start != -1 else ''

    # Parse buttons ( ) groups
    buttons = []
    targets = []
    parts = line[end+1:].replace(' ', '').replace('(', ' (').replace(')', ') ').replace('{', ' {').replace('}', '} ').split()
    i = 0
    while i < len(parts):
        if parts[i].startswith('('):
            button_str = parts[i][1:-1] if parts[i].endswith(')') else parts[i][1:]
            toggles = [int(x) for x in button_str.split(',') if x]
            buttons.append(toggles)
        elif parts[i].startswith('{'):
            target_str = parts[i][1:-1] if parts[i].endswith('}') else parts[i][1:]
            targets = [int(x) for x in target_str.split(',') if x]
        i += 1

    n_counters = len(targets)
    m = len(buttons)

    # Setup PuLP problem
    prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)

    # x_i >=0 integer
    x = [pulp.LpVariable(f"x{b}", lowBound=0, cat='Integer') for b in range(m)]

    # Objective: min sum x
    prob += pulp.lpSum(x)

    # Constraints: for each counter k, sum x_b * (1 if k in button_b) = target[k]
    for k in range(n_counters):
        prob += pulp.lpSum(x[b] for b in range(m) if k in buttons[b]) == targets[k]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # Get min presses
    min_presses = pulp.value(prob.objective)
    total_presses += int(min_presses) if min_presses is not None else 0

print("Total minimum presses:", total_presses)