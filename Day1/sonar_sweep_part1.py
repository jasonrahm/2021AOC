"""
Advent of Code - Day 1
Puzzle: Sonar Sweep Part 1
"""
with open('../input/sonar_sweep_data.txt', 'r') as f:
    depths: list = [int(x) for x in f.readlines()]

count: int = 0
for index, value in enumerate(depths):
    try:
        if depths[index + 1] > depths[index]:
            count += 1
    except IndexError:
        pass
print(count)
