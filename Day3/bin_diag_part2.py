"""
Advent of Code - Day 3
Puzzle: Binary Diagnostics Part 2
"""
import pandas as pd

####################
### NOT FINISHED ###
####################

with open('../input/binary_diagnostics_data.txt', 'r') as f:
    binary_digits: list = f.readlines()
    num_list: list = [str(x).strip() for x in binary_digits]

for i, num in enumerate(binary_digits):
    binary_digits[i] = [int(x) for x in num.strip()]

df = pd.DataFrame(binary_digits)

oxy_gen = ''
co2_scrub = ''
for i in range(0, 12):
    mcv = df[i].value_counts().idxmax()
    lcv = df[i].value_counts().idxmin()
    if mcv == lcv:
        mcv = 1
        lcv = 0
    oxy_gen += str(mcv)
    co2_scrub += str(lcv)

print(int(oxy_gen, 2) * int(co2_scrub, 2))
