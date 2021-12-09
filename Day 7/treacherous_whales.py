"""
Advent of Code - Day 7
Puzzle: The Treachery of Whales
"""
import statistics

from aocd.models import Puzzle


def part1(crab_positions):
    fuel = 0
    median = statistics.median(crab_positions)
    for position in crab_positions:
        fuel += abs(position - median)
    return fuel


# NOT MY SOLUTION, SAVED FOR STUDY
# From: https://github.com/fdu-edo/Advent-of-Code/blob/main/AoC-21/AoC-21%20py%20files/Aoc_2021_07.py
def cost(displacement):
    return int((displacement * (displacement +1)) / 2)


def part2(crab_positions):
    crab_positions = sorted(crab_positions)
    targets = range(crab_positions[0], crab_positions[-1])
    distances = [(target, sum([cost(abs(position - target)) for position in crab_positions])) for target in targets]
    return min(distances, key= lambda x: x[1])[1]


if __name__ == '__main__':
    year, day = 2021, 7
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    puzzle_data = [int(x) for x in puzzle.input_data.split(',')]

    result1 = part1(puzzle_data)
    result2 = part2([16,1,2,0,4,2,7,1,2,14])

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
