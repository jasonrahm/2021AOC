"""
Advent of Code - Day 1
Puzzle: Sonar Sweep Part 2
"""
with open('input/sonar_sweep_data.txt', 'r') as f:
    depths: list = [int(x) for x in f.readlines()]

count: int = 0
for index, value in enumerate(depths):
    try:
        if depths[index + 1] + \
           depths[index + 2] + \
           depths[index + 3] > \
           depths[index] + \
           depths[index + 1] + \
           depths[index + 2]:
            count += 1
    except IndexError:
        pass
print(count)

# Better IF statement: algebraic reduction
# if depths[index + 3] > depths[index]:
