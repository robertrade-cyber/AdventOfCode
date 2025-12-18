# Paste your full list into a file or directly here
lines = [line.strip() for line in open('Day1.txt') if line.strip()]  # or paste the data

# Part 1 (already accepted)
pos = 50
part1 = 0
for line in lines:
    dir = line[0]
    clicks = int(line[1:])
    delta = clicks if dir == 'R' else -clicks
    pos = (pos + delta) % 100
    if pos == 0:
        part1 += 1
print("Part 1:", part1)  # 1135

# Part 2
def count_passes(start, clicks, direction):
    if clicks == 0:
        return 0
    step = 1 if direction == 'R' else -1
    first_dist = 100 if start == 0 else (100 - start if step == 1 else start)
    if clicks < first_dist:
        return 0
    return 1 + (clicks - first_dist) // 100

pos = 50
part2 = 0
for line in lines:
    dir = line[0]
    clicks = int(line[1:])
    part2 += count_passes(pos, clicks, dir)
    delta = clicks if dir == 'R' else -clicks
    pos = (pos + delta) % 100

print("Part 2:", part2)  # 5677