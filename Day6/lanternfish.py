"""
Advent of Code - Day 6
Puzzle: Lanternfish
"""
from aocd.models import Puzzle


def part1(days, data):
    for _ in range(days):
        for i, timer in enumerate(data):
            if timer == 0:
                data[i] = 6
                data.append(9)
            else:
                data[i] -= 1
    return len(data)


def part2(days, data):
    ### Not complete ###
    # Advice: Build a dictionary for each "state" of fish, instead of tracking each fish
    pass


if __name__ == '__main__':
    year, day = 2021, 6
    puzzle = Puzzle(year, day)
    puzzle_data = [int(x) for x in puzzle.input_data.split(',')]

    res1 = part1(80, puzzle_data)
    res2 = part2(256, puzzle_data)
    #
    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {res1}')
    print(f'\tPart 2: {res2}')
