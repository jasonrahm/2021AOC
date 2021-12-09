"""
Advent of Code - Day 5
Puzzle: Hydrothermal Venture
"""
from collections import Counter
from helper_functions import input_data


def part1(thermal_lines):
    points = []
    for line in thermal_lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            relevant_points = [(x1, min(y1, y2) + x) for x in range(abs(y2 - y1) + 1)]
        elif y1 == y2:
            relevant_points = [(min(x1, x2) + x, y1) for x in range(abs(x2 - x1) + 1)]
        else:
            relevant_points = []
        points += relevant_points
    x = Counter(points)
    return len({k: x[k] for k in x.keys() if x[k] >= 2})


def part2(thermal_lines):
    points = []
    for line in thermal_lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            relevant_points = [(x1, min(y1, y2) + x) for x in range(abs(y2 - y1) + 1)]
        elif y1 == y2:
            relevant_points = [(min(x1, x2) + x, y1) for x in range(abs(x2 - x1) + 1)]
        elif x2 - x1 == y2 - y1:
            relevant_points = [(min(x1, x2) + x, min(y1, y2) + x) for x in range(abs(y2 - y1) + 1)]
        elif x2 - x1 == y1 - y2:
            relevant_points = [(min(x1, x2) + x, max(y1, y2) - x) for x in range(abs(y2 - y1) + 1)]
        else:
            relevant_points = []
        points += relevant_points
    x = Counter(points)
    return len({k: x[k] for k in x.keys() if x[k] >= 2})


if __name__ == '__main__':
    data = input_data('../input/hydrothermal_venture_data.txt')
    massaged_data = [[int(x) for x in l.replace(' -> ', ',').split(',')] for l in data]
    print(part1(massaged_data))
    print(part2(massaged_data))
