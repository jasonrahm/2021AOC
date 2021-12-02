"""
Advent of Code - Day 2
Puzzle: Dive Part 2
"""

with open('../input/dive_data.txt', 'r') as f:
    d_pos = 0
    h_pos = 0
    aim = 0
    for l in f.readlines():
        cmd = l.split(' ')[0]
        val = int(l.split(' ')[1])
        match cmd:
            case 'forward':
                h_pos += val
                d_pos += (aim * val)
            case 'down':
                aim += val
            case 'up':
                aim -= val

print(f'Product is {h_pos * d_pos}')
