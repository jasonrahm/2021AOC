"""
Advent of Code - Day 1
Puzzle: Sonar Sweep Part 1
"""
# from datetime import datetime
# from itertools import pairwise as pw

with open('input/sonar_sweep_data.txt', 'r') as f:
    depths: list = [int(x) for x in f.readlines()]

# My Solution
count: int = 0
for index, value in enumerate(depths):
    try:
        if depths[index + 1] > depths[index]:
            count += 1
    except IndexError:
        pass
print(count)

# # Learned Alternatives (code after the file read)
# print(sum([x < y for x, y in pw(depths)]))
