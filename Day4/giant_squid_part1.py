"""
Advent of Code - Day 4
Puzzle: Giant Squid Part 1
"""
import pandas as pd
import numpy as np
import sys

with open('../input/giant_squid_data.txt', 'r') as f:
    called_numbers: list = [int(x) for x in f.readline().rstrip().split(',')]
    next(f, None)
    lines = [x.strip() for x in f.readlines()]

    bingo_cards = []
    lines_tmp = lines.copy()
    for x in lines:
        card_lines = lines_tmp[0:5]
        for i, line in enumerate(card_lines):
            card_lines[i] = [int(x) for x in line.split()]
        bingo_cards.append(pd.DataFrame(card_lines))
        del lines_tmp[0:6]
        if len(lines_tmp) == 0:
            break

for n in called_numbers:
    for card in bingo_cards:
        card.replace(n, np.nan, inplace=True)
        bingo_row = card[card.isna().all(axis=1)].index.any()
        bingo_column = card[card.isna().all(axis=0)].index.any()
        if bingo_row | bingo_column:
            unmarked_sum = card.sum(numeric_only=True).sum()
            print(f'Final score: {unmarked_sum * n}')
            sys.exit()
