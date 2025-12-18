# Day 10 Part 1 - Factory Machine Initialization (fewest button presses)

import sys
from itertools import product

# Read the file
with open('Day10.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

total_presses = 0

for line in lines:
    # Parse the line
    parts = line.split()
    diagram = parts[0][1:-1]  # remove [ ]
    target = [1 if c == '#' else 0 for c in diagram]
    n_lights = len(target)

    # Buttons are the ( ) parts
    buttons = []
    i = 1
    while parts[i].startswith('('):
        button_str = parts[i][1:-1]  # remove ( )
        toggles = [int(x) for x in button_str.split(',') if x]
        buttons.append(toggles)
        i += 1

    m = len(buttons)

    # We need to solve A * x = target mod 2, where A is n_lights x m matrix
    # Each column of A is the toggle vector for a button
    # x is vector of presses mod 2 (since pressing twice = 0)
    # But we want minimal total presses (sum x_i, not mod 2)

    # Since pressing even times = 0 effect, odd = 1 effect
    # To minimize total presses, we try all 2^m possibilities for which buttons to press odd times
    # The total presses = number of buttons pressed odd times (since even presses can be 0)

    min_presses = sys.maxsize

    for mask in range(1 << m):  # 0 to 2^m - 1
        current = [0] * n_lights
        presses = 0
        for b in range(m):
            if mask & (1 << b):
                presses += 1
                for light in buttons[b]:
                    current[light] = 1 - current[light]
        if current == target:
            min_presses = min(min_presses, presses)

    total_presses += min_presses

print("Fewest total button presses:", total_presses)