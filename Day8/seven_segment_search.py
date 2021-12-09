"""
Advent of Code - Day 8
Puzzle: Seven Segment Search
"""
from aocd.models import Puzzle


def part1(data):
    unique_digits = []
    for entry in data:
        output_signal = entry[1].split(' ')
        for digit_value in output_signal:
            match len(digit_value):
                case 2 | 3 | 4 | 7:
                    unique_digits.append(digit_value)
    return len(unique_digits)


def part2(data):
    # TODO this is unfinished; and ugly. I shall wear the cone of shame.
    for entry in data:
        segment_position = {'t': [], 'ul': [], 'ur': [], 'm': [], 'll': [], 'lr': [], 'b': []}
        signal_pattern = entry[0]
        output_signal = entry[1]
        for signal in signal_pattern.split(' '):
            match len(signal):
                case 2:
                    segment_position['ur'].append(signal)
                    segment_position['lr'].append(signal)
                case 3:
                    segment_position['t'].append(signal)
                    segment_position['ur'].append(signal)
                    segment_position['lr'].append(signal)
                case 4:
                    segment_position['ul'].append(signal)
                    segment_position['ur'].append(signal)
                    segment_position['m'].append(signal)
                    segment_position['lr'].append(signal)
                case 7:
                    segment_position['t'].append(signal)
                    segment_position['ul'].append(signal)
                    segment_position['ur'].append(signal)
                    segment_position['m'].append(signal)
                    segment_position['ll'].append(signal)
                    segment_position['lr'].append(signal)
                    segment_position['b'].append(signal)
        # Set attempts ending in disaster
        # print(segment_position)
        # t = set(segment_position['t'][0]).intersection(*segment_position['t'])
        # ul = set(segment_position['ul'][0]).intersection(*segment_position['ul'])
        # ur = set(segment_position['ur'][0]).intersection(*segment_position['ur'])
        # m = set(segment_position['m'][0]).intersection(*segment_position['m'])
        # ll = set(segment_position['ll'][0]).intersection(*segment_position['ll'])
        # lr = set(segment_position['lr'][0]).intersection(*segment_position['lr'])
        # b = set(segment_position['b'][0]).intersection(*segment_position['b'])
        # print(t, ul, ur, m, ll, lr, b)
        # #Remove ur (or lr) from t
        # t = t.difference(ur)
        # #Remove t and ur from ul, m, ll, and b
        # ul = ul.difference(t)
        # m = ul.difference(t)
        # ll = ul.difference(t)
        # b = ul.difference(t)
        # print(t, ul, ur, m, ll, lr, b)
        # print('\n\n')
    return None


if __name__ == '__main__':
    year, day = 2021, 8
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    with open('test_data.txt', 'r') as f:
        puzzle_data = [x.split(' | ') for x in f.read().splitlines()]

    # puzzle_data = [x.split(' | ') for x in puzzle.input_data.split('\n')]
    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
